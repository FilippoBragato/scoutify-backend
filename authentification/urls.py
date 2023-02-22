from django.urls import path
from . import views

urlpatterns = [
    path("group/", views.getAllGroups),
    path('logout/', views.LogoutView.as_view(), name ='logout')
]
