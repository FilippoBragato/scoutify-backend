from django.urls import path
from . import views

urlpatterns = [
    path("scout/", views.getAllScout),
    path("scout/add/", views.addScout),
    path("scout/edit/<int:pk>", views.editScout),
    path("scout/delete/<int:pk>", views.deleteScout),
    path("patrol/", views.getAllPatrols),
    path("patrol/add/", views.addPatrol),
    path("patrol/edit/<int:pk>", views.editPatrol),
    path("patrol/delete/<int:pk>", views.deletePatrol),
    path("patrol/my/", views.getMyPatrol),
]
