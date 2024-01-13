from django.urls import path
from . import views

urlpatterns = [
    path("activity/", views.getAllActivity),
    path("activity/add/", views.addActivity),
    path("activity/edit/<int:pk>", views.editActivity),
    path("activity/delete/<int:pk>", views.deleteActivity),
    path("scoutpartecipation/", views.getAllScoutPartecipation),
    path("scoutpartecipation/add/", views.addScoutPartecipation),
    path("scoutpartecipation/edit/<int:pk>", views.editScoutPartecipation),
    path("scoutpartecipation/delete/<int:pk>", views.deleteScoutPartecipation),
]