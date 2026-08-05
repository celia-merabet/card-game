from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):

    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    score=models.IntegerField(default=0)

    games_played=models.IntegerField(default=0)

    games_won=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Game(models.Model):

    STATUS=[
        ("WAITING","En attente"),
        ("PLAYING","En cours"),
        ("FINISHED","Terminée")
    ]

    status=models.CharField(
        max_length=20,
        choices=STATUS,
        default="WAITING"
    )

    current_turn=models.IntegerField(default=0)

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game {self.id}"


class Card(models.Model):

    SUITS=[

        ("HEART","Heart"),

        ("DIAMOND","Diamond"),

        ("CLUB","Club"),

        ("SPADE","Spade")

    ]

    suit=models.CharField(
        max_length=20,
        choices=SUITS
    )

    value=models.IntegerField()

    game=models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.value} {self.suit}"


class MoveLog(models.Model):

    game=models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    player=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action=models.CharField(max_length=100)

    created=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.action