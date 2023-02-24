from django.urls import path
from . import views

urlpatterns = [
    path("article/", views.getAllArticles),
    path("article/add/", views.addArticle),
    path("article/edit/<int:pk>/", views.editArticle),
    path("article/delete/<int:pk>/", views.deleteArticle),
]
