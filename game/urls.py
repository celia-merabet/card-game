from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [ # Accueil 
    path("", views.home, name="home"), 
    
    # Connexion
    path( "login/", auth_views.LoginView.as_view( template_name="game/login.html" ), name="login" ), # Inscription 
    
    path( "register/", views.register, name="register" ), 

    # Déconnexion 
    path( "logout/", auth_views.LogoutView.as_view(), name="logout" ), ]