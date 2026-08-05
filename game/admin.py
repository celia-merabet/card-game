from django.contrib import admin

from .models import (
    Profile,
    Game,
    Card,
    Deck,
    MoveLog
)



admin.site.register(Profile)

admin.site.register(Game)

admin.site.register(Card)

admin.site.register(Deck)

admin.site.register(MoveLog)