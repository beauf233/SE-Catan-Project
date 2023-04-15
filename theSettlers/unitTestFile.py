import unittest
from player import Player
from cardTypes import ResCard,DevCard
from runGame import GameRunner

class testSetAndGetCards(unittest.TestCase):
    def runTest(self):
        currentGame = GameRunner(1)
        testResCard = ResCard(1)
        player = Player(currentGame, 1)
        listOfCards = [testResCard]
        player.addResCards(listOfCards)
        #print("test:" +str(player.hasRescards(listOfCards)))
        self.assertEqual(player.hasRescards(listOfCards), True, "card not present")

unittest.main()
