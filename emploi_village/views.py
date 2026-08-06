from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from dal import autocomplete
from .models import Personnels, Ville, Metier, Actualite
from .forms import VilleForm, MetierForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import (
    VilleForm,
    MetierForm,
    ConnexionForm,
    ModifierPersonnelForm,
    ActualiteForm
)

def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_superuser, login_url='connexion')
def admin_page(request):

    nombre_personnels = Personnels.objects.count()
    nombre_villes = Ville.objects.count()
    nombre_metiers = Metier.objects.count()
    nombre_actualites = Actualite.objects.count()
    nombre_utilisateurs = User.objects.count()

    context = {
        'nombre_personnels': nombre_personnels,
        'nombre_villes': nombre_villes,
        'nombre_metiers': nombre_metiers,
        'nombre_actualites': nombre_actualites,
        'nombre_utilisateurs': nombre_utilisateurs,
    }

    return render(
        request,
        'admin1.html',
        context
    )

def pagea(request):
    ville_list = Ville.objects.all()
    return render(request, 'pagea.html', {'ville_list': ville_list})

def admin1(request):
    return render(request, 'admin1.html')

def inscription(request):
    metier_list = Metier.objects.all()
    return render(request, 'inscription.html', {'metier_list': metier_list})

def teste0(request):
    context = {"metier": Metier.objects.all()}
    return render(request, 'teste0.html', )

# Afficher une ville
def affiche_village(request):
    ville_nom = request.GET.get('ville')  # nom du village sélectionné
    ville_trouvee = Ville.objects.filter(nomv__iexact=ville_nom).first()

    if ville_trouvee:
        context = {'ville': ville_trouvee}
        return render(request, 'affiche_village.html', context)
    else:
        return render(request, 'affiche_village.html', {
            'erreur': "Aucune information trouvée pour ce village."
        })

# Afficher les métiers
def affiche_metier(request):
    context = {"metier": Metier.objects.all()}
    return render(request, 'affiche_metier.html', context)

# Liste du personnel
def list_personnel(request):
    idm = request.GET.get('id')  # Récupère l'ID du métier depuis la requête GET
    personnels_list = []

    if idm:
        try:
            idm_int = int(idm)
            personnels_list = Personnels.objects.filter(metier=idm_int)  # Correction ici
        except ValueError:
            personnels_list = []  # Si l'ID n'est pas un entier, on retourne une liste vide

    context = {
        'list_personnel': personnels_list
    }
    return render(request, 'list_personnel.html', context)

# Inscription du personnel
#def inscription1(request):
 #   if request.method == 'POST':
  #      form = PersonnelsForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('pagea')  # ou vers une page de succès
    #else:
      #  form = PersonnelsForm()

    #villes = Ville.objects.all()
    #metiers = Metier.objects.all()

    #return render(request, 'inscription.html', {
     #   'form': form,
      #  'villes': villes,
       # 'metiers': metiers
   # })

# Vue pour l'autocomplétion des villes
class VilleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Ville.objects.all()
        if self.q:
            qs = qs.filter(nom__icontains=self.q)
        return qs

class MetierAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Metier.objects.all()
        if self.q:
            qs = qs.filter(nom__icontains=self.q)
        return qs


def inscription_custom(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        tel = request.POST.get('tel')
        gmail = request.POST.get('gmail')
        daten = request.POST.get('daten')
        niveaup = request.POST.get('niveaup')
        famille = request.POST.get('famille')
        residence = request.POST.get('residence')
        ville_nom = request.POST.get('ville')
        metier_noms_list = request.POST.getlist('metier[]')  # Récupérer les métiers comme une liste

        try:
            # Création de la ville si elle n'existe pas
            ville, _ = Ville.objects.get_or_create(nomv=ville_nom)

            # Création du personnel (sans les métiers pour le moment)
            personnel = Personnels(
                nom=nom,
                tel=tel,
                gmail=gmail,
                daten=daten,
                niveaup=niveaup,
                famille=famille,
                residence=residence,
                ville=ville
            )
            personnel.save()

            # Traitement des métiers saisis par l'utilisateur
            for metier_nom in metier_noms_list:
                if metier_nom:
                    metier, _ = Metier.objects.get_or_create(nomm=metier_nom.strip())
                    # Ajouter chaque métier au personnel (ManyToMany)
                    personnel.metier.add(metier)

            messages.success(request, "Inscription réussie.")
            return redirect('inscription_custom')

        except Exception as e:
            messages.error(request, f"Erreur lors de l'inscription : {str(e)}")
            return redirect('inscription_custom')

    villes = Ville.objects.all()
    metiers = Metier.objects.all()
    return render(request, 'inscription_custom.html', {
        'villes': villes,
        'metiers': metiers,
    })

def afficher_personnels(request):
    personnels = Personnels.objects.all()
    return render(request, 'afficher_personnels.html', {'personnels': personnels})

def supprimer_personnel(request, personnel_id):
    personnel = Personnels.objects.get(id=personnel_id)
    personnel.delete()
    return redirect('afficher_personnels')

    # Vue pour ajouter un village
def ajoute_village(request):
    if request.method == 'POST':
        form = VilleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagea')  # Redirection vers la page d'accueil après ajout
    else:
        form = VilleForm()
    return render(request, 'ajoute_village.html', {'form': form})

# Vue pour ajouter un métier
def ajoute_metier(request):
    if request.method == 'POST':
        form = MetierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajoute_metier')  # Redirection vers la page d'accueil après ajout
    else:
        form = MetierForm()
    return render(request, 'ajoute_metier.html', {'form': form})

def pagea(request):

    images = [
        {'fichier': 'ville8.jpg', 'nom': 'Pompe Du Village'},
        {'fichier': 'ville6.jpg', 'nom': 'Village'},
        {'fichier': 'ville4.jpg', 'nom': 'Stard'},
        {'fichier': 'ville2.jpg', 'nom': 'Village 1'},
        {'fichier': 'ville10.jpg', 'nom': 'Village 2'},
        {'fichier': 'ville11.jpg', 'nom': 'Village 3'},
        {'fichier': 'ville9.jpg', 'nom': 'Village 4'},
        {'fichier': 'ville7.jpg', 'nom': 'Village 5'},
        {'fichier': 'ville12.jpg', 'nom': 'Village 6'},
    ]

    return render(
        request,
        'pagea.html',
        {'images': images}
    )


# ============================================================
# PAGE INFORMATIONS
# ============================================================

def infot(request):

    ville_list = Ville.objects.all()

    return render(
        request,
        'infot.html',
        {
            'ville_list': ville_list
        }
    )

# ============================================================

# CONNEXION AVEC ADRESSE E-MAIL + MOT DE PASSE

# ============================================================

def connexion_view(request):

    if request.method == "POST":

        form = ConnexionForm(request.POST)

        if form.is_valid():

            gmail = form.cleaned_data['gmail'].strip().lower()
            password = form.cleaned_data['password']

            utilisateur = User.objects.filter(
                email__iexact=gmail
            ).first()

            if utilisateur is None:
                messages.error(
                    request,
                    "Adresse e-mail ou mot de passe incorrect."
                )
                return render(
                    request,
                    'connexion.html',
                    {'form': form}
                )

            user = authenticate(
                request,
                username=utilisateur.username,
                password=password
            )

            if user is None:
                messages.error(
                    request,
                    "Adresse e-mail ou mot de passe incorrect."
                )
                return render(
                    request,
                    'connexion.html',
                    {'form': form}
                )

            if not user.is_active:
                messages.error(
                    request,
                    "Votre compte est désactivé."
                )
                return render(
                    request,
                    'connexion.html',
                    {'form': form}
                )

            personnel = Personnels.objects.filter(
                gmail__iexact=gmail
            ).first()

            if personnel is None:
                messages.error(
                    request,
                    "Aucun personnel associé à ce compte."
                )
                return render(
                    request,
                    'connexion.html',
                    {'form': form}
                )

            login(request, user)

            request.session['user_id'] = personnel.id
            request.session['user_email'] = personnel.gmail

            messages.success(
                request,
                f"Bienvenue {personnel.nom}."
            )

            # Retour à la page demandée avant connexion
            next_url = (
                request.POST.get('next')
                or request.GET.get('next')
            )

            if next_url:
                return redirect(next_url)

            # Destination par défaut
            return redirect('modifier')

    else:
        form = ConnexionForm()

    return render(
        request,
        'connexion.html',
        {'form': form}
    )
# ============================================================
# MODIFICATION DES INFORMATIONS DU PERSONNEL CONNECTÉ
# ============================================================

@login_required(login_url='connexion')
def modifier_view(request):

    # Récupérer l'identifiant du personnel connecté
    personnel_id = request.session.get('user_id')

    if not personnel_id:

        messages.error(
            request,
            "Aucun personnel associé à votre compte."
        )

        logout(request)

        return redirect('connexion')

    # Récupérer le personnel
    personnel = get_object_or_404(
        Personnels,
        id=personnel_id
    )

    # Vérifier que le compte Django correspond
    # bien au personnel connecté
    if not request.user.is_authenticated:

        return redirect('connexion')

    if request.user.email.lower() != personnel.gmail.lower():

        messages.error(
            request,
            "Votre compte n'est pas associé à ce personnel."
        )

        logout(request)

        return redirect('connexion')

    # ========================================================
    # ENREGISTREMENT DES MODIFICATIONS
    # ========================================================

    if request.method == "POST":

        form = ModifierPersonnelForm(
            request.POST,
            request.FILES,
            instance=personnel
        )

        if form.is_valid():

            personnel_modifie = form.save()

            # ------------------------------------------------
            # Synchroniser le Gmail avec le compte Django
            # ------------------------------------------------

            nouvelle_adresse = (
                personnel_modifie.gmail
                .strip()
                .lower()
            )

            # Vérifier si l'adresse a changé
            if nouvelle_adresse != request.user.email.lower():

                # Vérifier que le nouvel e-mail
                # n'est pas déjà utilisé
                autre_user = User.objects.filter(
                    email__iexact=nouvelle_adresse
                ).exclude(
                    id=request.user.id
                ).first()

                if autre_user:

                    messages.error(
                        request,
                        "Cette adresse e-mail est déjà utilisée "
                        "par un autre compte."
                    )

                    return render(
                        request,
                        'modifier.html',
                        {
                            'form': form,
                            'personnel': personnel
                        }
                    )

                # Modifier l'e-mail du compte Django
                request.user.email = nouvelle_adresse

                # Comme le username est utilisé pour
                # l'authentification, on le synchronise également
                request.user.username = nouvelle_adresse

                request.user.save()

                # Mettre à jour la session
                request.session['user_email'] = nouvelle_adresse

            messages.success(
                request,
                "Vos informations ont été mises à jour avec succès."
            )

            return redirect('pagea')

    else:

        form = ModifierPersonnelForm(
            instance=personnel
        )

    return render(
        request,
        'modifier.html',
        {
            'form': form,
            'personnel': personnel
        }
    )
# ============================================================
# AFFICHAGE DES ACTUALITES
# ============================================================

def actualites_view(request):

    actualites = Actualite.objects.order_by(
        '-date_pub'
    )

    return render(
        request,
        'actualites.html',
        {
            'actualites': actualites
        }
    )
# ============================================================
# AJOUTER UNE ACTUALITE
# ============================================================

@user_passes_test(
    lambda u: u.is_authenticated and u.is_superuser,
    login_url='connexion'
)
def ajouter_actualite(request):

    if request.method == 'POST':

        form = ActualiteForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Actualité publiée avec succès."
            )

            return redirect('actualites')

    else:
        form = ActualiteForm()

    return render(
        request,
        'ajouter_actualite.html',
        {'form': form}
    )

# ============================================================
# VÉRIFICATION ADMINISTRATEUR
# ============================================================

def est_admin(user):
    return user.is_authenticated and user.is_superuser


# ============================================================
# MODIFIER UNE ACTUALITÉ
# ADMIN UNIQUEMENT
# ============================================================

@user_passes_test(
    est_admin,
    login_url='connexion'
)
def modifier_actualite(request, actualite_id):

    actualite = get_object_or_404(
        Actualite,
        id=actualite_id
    )

    if request.method == 'POST':

        form = ActualiteForm(
            request.POST,
            request.FILES,
            instance=actualite
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Actualité modifiée avec succès."
            )

            return redirect('actualites')

    else:

        form = ActualiteForm(
            instance=actualite
        )

    return render(
        request,
        'modifier_actualite.html',
        {
            'form': form,
            'actualite': actualite
        }
    )


# ============================================================
# SUPPRIMER UNE ACTUALITÉ
# ADMIN UNIQUEMENT
# ============================================================

@user_passes_test(
    est_admin,
    login_url='connexion'
)
def supprimer_actualite(request, actualite_id):

    actualite = get_object_or_404(
        Actualite,
        id=actualite_id
    )

    # Suppression uniquement avec POST
    if request.method == 'POST':

        # Supprimer le fichier image
        if actualite.image:
            actualite.image.delete(save=False)

        # Supprimer le fichier vidéo
        if actualite.video:
            actualite.video.delete(save=False)

        actualite.delete()

        messages.success(
            request,
            "Actualité supprimée avec succès."
        )

    return redirect('actualites')

def deconnexion_view(request):
    logout(request)
    return redirect('connexion')