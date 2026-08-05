from django.test import TestCase

from .game_engine import CardGameEngine



class EngineTest(TestCase):


    def test_create_deck(self):

        engine=CardGameEngine()

        deck=engine.create_deck()


        self.assertEqual(
            len(deck),
            52
        )



    def test_shuffle(self):

        engine=CardGameEngine()

        deck=engine.create_deck()

        shuffled=engine.shuffle(deck)


        self.assertEqual(
            len(shuffled),
            52
        )



    def test_compare(self):

        engine=CardGameEngine()


        result=engine.compare_cards(
            {
                "value":10
            },
            {
                "value":5
            }
        )


        self.assertEqual(
            result,
            "PLAYER1"
        )