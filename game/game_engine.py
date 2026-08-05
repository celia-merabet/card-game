
import random


class CardGameEngine:


    def create_deck(self):

        suits=[
            "HEART",
            "DIAMOND",
            "CLUB",
            "SPADE"
        ]

        values=list(range(1,14))

        deck=[]

        for suit in suits:
            for value in values:
                deck.append(
                    {
                    "suit":suit,
                    "value":value
                    }
                )

        return deck



    def shuffle(self,deck):

        random.shuffle(deck)

        return deck



    def compare_cards(self,card1,card2):

        if card1["value"] > card2["value"]:
            return 1

        if card1["value"] < card2["value"]:
            return -1

        return 0


