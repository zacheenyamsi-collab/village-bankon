from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path(
        'admin1/',
        views.admin_page,
        name='admin_page'
    ),

    path(
        'infot/',
        views.infot,
        name='infot'
    ),

    path(
        'pagea/',
        views.pagea,
        name='pagea'
    ),

    path(
        'connexion/',
        views.connexion_view,
        name='connexion'
    ),

    path(
        'deconnexion/',
        views.deconnexion_view,
        name='deconnexion'
    ),

]