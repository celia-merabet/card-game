from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm


def index(request):
    """Page d'accueil."""
    return render(request, "game/index.html")


@login_required
def game_view(request):
    """Page principale du jeu."""
    return render(request, "game/game.html")


@login_required
def profile(request):
    """Page du profil utilisateur."""
    return render(request, "game/profile.html")


def register(request):
    """Inscription d'un nouvel utilisateur."""

    if request.user.is_authenticated:
        return redirect("game:index")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Votre compte a été créé avec succès."
            )

            return redirect("game:index")
    else:
        form = RegisterForm()

    return render(
        request,
        "game/register.html",
        {"form": form}
    )