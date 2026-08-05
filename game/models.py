
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



class Game(models.Model):

    STATUS=[
        ("WAITING","EN_ATTENTE"),
        ("PLAYING","EN_COURS"),
        ("FINISHED","TERMINEE")
    ]

    status=models.CharField(
        max_length=20,
        choices=STATUS,
        default="WAITING"
    )

    current_turn=models.IntegerField(default=0)



class Card(models.Model):

    suit=models.CharField(max_length=20)

    value=models.IntegerField()

    game=models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )



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

