from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.getAllFantatask),
    path("task/add/", views.addFantaTask),
    path("task/edit/<int:pk>/", views.editFantaTask),
    path("task/delete/<int:pk>/", views.deleteFantaTask),
    path("complete/", views.getAllScoutCompleteTask),
    path("complete/validate/", views.getScoutCompleteTaskToValidate),
    path("complete/add/", views.addScoutCompleteTask),
    path("complete/edit/<int:pk>/", views.editScoutCompleteTask),
    path("complete/delete/<int:pk>/", views.deleteScoutCompleteTask),
]
