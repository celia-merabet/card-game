
from django.test import TestCase
from .game_engine import CardGameEngine



class GameTest(TestCase):


    def test_deck_creation(self):

        engine=CardGameEngine()

        deck=engine.create_deck()

        self.assertEqual(
            len(deck),
            52
        )

