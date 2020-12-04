import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.cards = []
        # set up Cards
        self.card_ace = Card("Club", 1)
        self.cards.append(self.card_ace)

        self.card_5 = Card("Spade", 5)
        self.cards.append(self.card_5)

        self.card_10 = Card("Diamond", 10)
        self.cards.append(self.card_10)

        self.card_king = Card("Heart", 13)
        self.cards.append(self.card_king)

        # set up game
        self.card_game = CardGame()



    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_ace))


    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_5))


    def test_highest_card_first_card(self):
        self.assertEqual(self.card_10, self.card_game.highest_card(self.card_10, self.card_5))


    def test_highest_card_second_card(self):
        self.assertEqual(self.card_king, self.card_game.highest_card(self.card_10, self.card_king))


    def test_cards_total(self):
        self.assertEqual("You have a total of29", self.card_game.cards_total(self.cards))


