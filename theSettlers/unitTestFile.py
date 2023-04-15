import unittest
from player import Player
from cardTypes import ResCard,DevCard
from runGame import GameRunner

class testPlayerClass(unittest.TestCase):
    
    def testAddRemoveHasResCard(self):
        currentGame = GameRunner(1)
        testResCard = ResCard(1)
        testResCard2 = ResCard(1)
        player = Player(currentGame, 1)
        listOfCards = [testResCard]
        player.addResCards(listOfCards)
        #print("test:" +str(player.hasRescards(listOfCards)))
        self.assertEqual(player.hasRescards(listOfCards), True, "card not present")
        listOfCards.append(testResCard2)
        self.assertEqual(player.hasRescards(listOfCards), False, "card not present")
        listOfCardsToCheck = listOfCards
        del listOfCards[1]
        player.addResCards(listOfCards)
        self.assertEqual(player.hasRescards(listOfCardsToCheck), True, "card not present")
        player.removeResCards(listOfCards)
        listOfCardsToCheck = [testResCard]
        self.assertEqual(player.hasRescards(listOfCardsToCheck), True)

        
        testDevCard1 = DevCard(1)
        del listOfCards[:]
        listOfCards.append(testDevCard1)
        player.addResCards(listOfCards)
        
        self.assertEqual(player.hasRescards(listOfCards), False)
    
    def testAddHasDevCardTrueCase(self):
        currentGame = GameRunner(1)
        testDevCard = DevCard(1)
        testPlayer = Player(currentGame, 1)
        listOfCards = [testDevCard]
        testPlayer.addDevCard(listOfCards)
        self.assertEqual(testPlayer.hasDevCards(listOfCards), True, "card not present")
unittest.main()