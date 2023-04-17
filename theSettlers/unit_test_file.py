import unittest
from player import Player
from card_types import ResCard,DevCard
from run_game import GameRunner

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

class testRunGame(unittest.TestCase):
    def testShuffleDevelopDeck(self):
        testGameRunner = GameRunner(3)
        testDevelopCardDeck = testGameRunner.shuffleDevelopCards()
        self.assertEqual(len(testDevelopCardDeck), 25)
    
    def testPlayerPickUpDevCard(self):
        testGameRunner = GameRunner(2)
        testDevCard = testGameRunner.developDeck[0]
        testGameRunner.pickUpDevCard(0)
        testPlayer = Player
        testPlayer = testGameRunner.getPlayer(0)
        
        
        self.assertEqual(testPlayer.hasCard())

unittest.main()