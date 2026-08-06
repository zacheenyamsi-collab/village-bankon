from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Personnels, Ville, Metier, Actualite


# ============================================================
# FORMULAIRE DE CRÉATION D'UTILISATEUR
# ============================================================

class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                'placeholder': 'Mot de passe'
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirmation du mot de passe",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                'placeholder': 'Confirmer le mot de passe'
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields


# ============================================================
# FORMULAIRE VILLE
# ============================================================

class VilleForm(forms.ModelForm):

    class Meta:
        model = Ville

        fields = [
            'nomv',
            'histoire',
        ]

        widgets = {

            'nomv': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nom du village'
                }
            ),

            'histoire': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Histoire du village'
                }
            ),
        }


# ============================================================
# FORMULAIRE MÉTIER
# ============================================================

class MetierForm(forms.ModelForm):

    class Meta:
        model = Metier

        fields = [
            'nomm',
            'niveaum',
        ]

        widgets = {

            'nomm': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nom du métier'
                }
            ),

            'niveaum': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Niveau requis'
                }
            ),
        }


# ============================================================
# FORMULAIRE DE CONNEXION
# ============================================================

class ConnexionForm(forms.Form):

    gmail = forms.EmailField(
        label="Adresse e-mail",

        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Votre adresse e-mail',
                'autocomplete': 'email'
            }
        )
    )

    password = forms.CharField(
        label="Mot de passe",

        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Votre mot de passe',
                'autocomplete': 'current-password'
            }
        )
    )


# ============================================================
# FORMULAIRE DE MODIFICATION DU PERSONNEL
# ============================================================

class ModifierPersonnelForm(forms.ModelForm):

    class Meta:

        model = Personnels

        fields = [
            'nom',
            'tel',
            'gmail',
            'daten',
            'niveaup',
            'famille',
            'residence',
            'ville',
            'metier',
            'cv',
        ]

        widgets = {

            # ------------------------------------------------
            # NOM
            # ------------------------------------------------

            'nom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nom complet'
                }
            ),

            # ------------------------------------------------
            # TÉLÉPHONE
            # ------------------------------------------------

            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numéro de téléphone'
                }
            ),

            # ------------------------------------------------
            # EMAIL
            # ------------------------------------------------

            'gmail': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Adresse e-mail',
                    'autocomplete': 'email'
                }
            ),

            # ------------------------------------------------
            # DATE DE NAISSANCE
            # ------------------------------------------------

            'daten': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            # ------------------------------------------------
            # NIVEAU D'ÉTUDE
            # ------------------------------------------------

            'niveaup': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Niveau d’étude'
                }
            ),

            # ------------------------------------------------
            # SITUATION FAMILIALE
            # ------------------------------------------------

            'famille': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Situation familiale'
                }
            ),

            # ------------------------------------------------
            # RÉSIDENCE
            # ------------------------------------------------

            'residence': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Lieu de résidence'
                }
            ),

            # ------------------------------------------------
            # VILLAGE
            # ------------------------------------------------

            'ville': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            # ------------------------------------------------
            # MÉTIERS
            # ------------------------------------------------

            'metier': forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'size': '4'
                }
            ),

            # ------------------------------------------------
            # CV
            # ------------------------------------------------

            'cv': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': '.pdf,.doc,.docx'
                }
            ),
        }


# ============================================================
# FORMULAIRE ACTUALITÉ
# ============================================================

class ActualiteForm(forms.ModelForm):

    class Meta:

        model = Actualite

        fields = [
            'titre',
            'contenu',
            'image',
            'video',
        ]

        widgets = {

            'titre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Titre de l’actualité'
                }
            ),

            'contenu': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 7,
                    'placeholder': 'Écrivez le contenu de l’actualité...'
                }
            ),

            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*'
                }
            ),

            'video': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'video/*'
                }
            ),
        }