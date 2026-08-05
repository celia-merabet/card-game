from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm

from .models import Profile,Game

from .game_engine import CardGameEngine



def index(request):

    return render(
        request,
        "game/index.html"
    )




def register(request):

    if request.method=="POST":

        form=RegisterForm(request.POST)


        if form.is_valid():

            user=form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()


            Profile.objects.create(
                user=user
            )


            login(
                request,
                user
            )


            return redirect("profile")


    else:

        form=RegisterForm()


    return render(
        request,
        "game/register.html",
        {
            "form":form
        }
    )





def login_view(request):

    if request.method=="POST":

        form=AuthenticationForm(
            request,
            data=request.POST
        )


        if form.is_valid():

            user=form.get_user()

            login(
                request,
                user
            )

            return redirect("profile")


    else:

        form=AuthenticationForm()


    return render(
        request,
        "game/login.html",
        {
            "form":form
        }
    )





@login_required
def profile(request):

    return render(
        request,
        "game/profile.html"
    )





@login_required
def game(request):

    engine=CardGameEngine()

    cards=engine.shuffle(
        engine.create_deck()
    )


    return render(
        request,
        "game/game.html",
        {
            "cards":cards[:5]
        }
    )