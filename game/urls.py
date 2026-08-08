from django.urls import path

from . import views


app_name = "game"


urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),

    path(
        "game/",
        views.game_view,
        name="game",
    ),

    path(
        "profile/",
        views.profile,
        name="profile",
    ),

    path(
        "register/",
        views.register,
        name="register",
    ),
]