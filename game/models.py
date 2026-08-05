from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(
        default=0
    )

    games_played = models.IntegerField(
        default=0
    )

    games_won = models.IntegerField(
        default=0
    )


    def __str__(self):

        return self.user.username



class Game(models.Model):

    STATUS = (

        ("WAITING", "En attente"),

        ("PLAYING", "En cours"),

        ("FINISHED", "Terminée"),

    )


    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="WAITING"
    )


    player1 = models.ForeignKey(
        User,
        related_name="games_created",
        on_delete=models.CASCADE
    )


    player2 = models.ForeignKey(
        User,
        related_name="games_joined",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    current_turn = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="current_games"
    )


    winner = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="wins"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"Partie {self.id}"



class Deck(models.Model):

    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE
    )


    remaining_cards = models.JSONField(
        default=list
    )


    def shuffle(self):

        import random

        random.shuffle(
            self.remaining_cards
        )

        self.save()



    def draw(self):

        if len(self.remaining_cards) > 0:

            card = self.remaining_cards.pop()

            self.save()

            return card

        return None




class Card(models.Model):

    SUITS = (

        ("HEART", "♥ Coeur"),

        ("DIAMOND", "♦ Carreau"),

        ("CLUB", "♣ Trèfle"),

        ("SPADE", "♠ Pique"),

    )


    suit = models.CharField(
        max_length=20,
        choices=SUITS
    )


    value = models.IntegerField()


    owner = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )


    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )


    def __str__(self):

        return f"{self.value} {self.suit}"




class MoveLog(models.Model):


    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )


    player = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    action = models.CharField(
        max_length=255
    )


    card_played = models.CharField(
        max_length=50,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.action