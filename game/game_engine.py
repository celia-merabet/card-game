import random



class CardGameEngine:


    SUITS = [

        "HEART",

        "DIAMOND",

        "CLUB",

        "SPADE"

    ]


    VALUES = list(range(1,14))



    def create_deck(self):

        deck=[]


        for suit in self.SUITS:

            for value in self.VALUES:

                deck.append(
                    {
                        "suit":suit,
                        "value":value
                    }
                )


        return deck



    def shuffle(self, deck):

        random.shuffle(deck)

        return deck




    def distribute(self, deck):

        player1=[]

        player2=[]


        for index,card in enumerate(deck):

            if index % 2 == 0:

                player1.append(card)

            else:

                player2.append(card)


        return player1,player2




    def compare_cards(
            self,
            card1,
            card2
    ):


        if card1["value"] > card2["value"]:

            return "PLAYER1"


        elif card1["value"] < card2["value"]:

            return "PLAYER2"


        else:

            return "DRAW"



    def calculate_score(
            self,
            winner
    ):


        if winner == "PLAYER1":

            return 1


        if winner == "PLAYER2":

            return 1


        return 0




    def check_end_game(
            self,
            hand1,
            hand2
    ):


        if len(hand1)==0:

            return "PLAYER2"


        if len(hand2)==0:

            return "PLAYER1"


        return None