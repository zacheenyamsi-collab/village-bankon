from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from emploi_village import views

from emploi_village.views import (
    VilleAutocomplete,
    MetierAutocomplete,
    inscription_custom,
    afficher_personnels,
    supprimer_personnel,
    admin_page,
    ajoute_village,
    ajoute_metier,
)


urlpatterns = [

    # ============================================================
    # ADMIN
    # ============================================================

    path(
        'admin/',
        admin.site.urls
    ),
    path('admin1/', views.admin_page, name='admin_page'),

    path(
        'admin1/',
        admin_page,
        name='admin1'
    ),

    # ============================================================
    # ACCUEIL
    # ============================================================

    path(
        '',
        views.pagea,
        name='pagea'
    ),

    # ============================================================
    # INFORMATIONS
    # ============================================================

    path(
        'teste0/',
        views.teste0,
        name='teste0'
    ),

    path(
        'infot/',
        views.infot,
        name='infot'
    ),

    path(
        'affiche_village/',
        views.affiche_village,
        name='affiche_village'
    ),

    path(
        'affiche_metier/',
        views.affiche_metier,
        name='affiche_metier'
    ),

    # ============================================================
    # PERSONNELS
    # ============================================================

    path(
        'list_personnel/',
        views.list_personnel,
        name='list_personnel'
    ),

    path(
        'inscription_custom/',
        inscription_custom,
        name='inscription_custom'
    ),

    path(
        'inscription/',
        inscription_custom,
        name='inscription'
    ),

    path(
        'afficher_personnels/',
        afficher_personnels,
        name='afficher_personnels'
    ),

    path(
        'supprimer_personnel/<int:personnel_id>/',
        supprimer_personnel,
        name='supprimer_personnel'
    ),

    # ============================================================
    # AUTOCOMPLETION
    # ============================================================

    path(
        'ville-autocomplete/',
        VilleAutocomplete.as_view(),
        name='ville-autocomplete'
    ),

    path(
        'metier-autocomplete/',
        MetierAutocomplete.as_view(),
        name='metier-autocomplete'
    ),

    # ============================================================
    # VILLAGES ET METIERS
    # ============================================================

    path(
        'ajoute_village/',
        ajoute_village,
        name='ajoute_village'
    ),

    path(
        'ajoute_metier/',
        ajoute_metier,
        name='ajoute_metier'
    ),

    # ============================================================
    # CONNEXION
    # ============================================================

    path(
        'connexion/',
        views.connexion_view,
        name='connexion'
    ),

    path(
        'modifier/',
        views.modifier_view,
        name='modifier'
    ),

    path(
        'deconnexion/',
        views.deconnexion_view,
        name='deconnexion'
    ),

    # ============================================================
    # ACTUALITES
    # ============================================================

   path(
    'actualites/',
    views.actualites_view,
    name='actualites'
    ),

    path(
        'actualites/ajouter/',
        views.ajouter_actualite,
        name='ajouter_actualite'
    ),

    path(
        'actualites/<int:actualite_id>/modifier/',
        views.modifier_actualite,
        name='modifier_actualite'
    ),

    path(
        'actualites/<int:actualite_id>/supprimer/',
        views.supprimer_actualite,
        name='supprimer_actualite'
    ),
]


# ============================================================
# FICHIERS MEDIA ET STATIC EN DEVELOPPEMENT
# ============================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )