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
        self.assertEqual(player.hasResCards(listOfCards), True, "card not present")
        listOfCards.append(testResCard2)
        self.assertEqual(player.hasResCards(listOfCards), False, "card not present")
        listOfCardsToCheck = listOfCards
        del listOfCards[1]
        player.addResCards(listOfCards)
        self.assertEqual(player.hasResCards(listOfCardsToCheck), True, "card not present")
        player.removeResCards(listOfCards)
        listOfCardsToCheck = [testResCard]
        self.assertEqual(player.hasResCards(listOfCardsToCheck), True)
    
        
        testDevCard1 = DevCard(1)
        del listOfCards[:]
        listOfCards.append(testDevCard1)
        player.addResCards(listOfCards)
        
        self.assertEqual(player.hasResCards(listOfCards), False)
    
    def testAddHasDevCardTrueCase(self):
        currentGame = GameRunner(1)
        testDevCard = DevCard(1)
        testPlayer = Player(currentGame, 1)
        listOfCards = [testDevCard]
        testPlayer.addDevCard(listOfCards)
        self.assertEqual(testPlayer.hasDevCards(listOfCards), True, "card not present")

class testRunGame(unittest.TestCase):
    #Tests the shuffleDevelopCards method
    def testShuffleDevelopDeck(self):
        testGameRunner = GameRunner(3)
        testDevelopCardDeck = testGameRunner.shuffleDevelopCards()
        self.assertEqual(len(testDevelopCardDeck), 25)
    
    #Tests the pickUpDevCard in gameRunner by using the hasDevCards function in player
    #Tests the getPlayer method
    def testPlayerPickUpDevCard(self):
        testGameRunner = GameRunner(2)
        testDevCard = testGameRunner.developDeck[24]
        testGameRunner.pickUpDevCard(0)
        #testPlayer = Player
        testPlayer = testGameRunner.getPlayer(0)
        self.assertEqual(testPlayer.hasDevCards(testDevCard), True)

    #Testing the intialisation of the hexagons
    def testInnitHexagons(self):
        testGameRunner = GameRunner(1)
        print("Number of hexagons:"+ str(len(testGameRunner.hexagons)))
        self.assertEqual(len(testGameRunner.hexagons), 19)
    #Tests the dice roll method
    def testRollDice(self):
        testGameRunner = GameRunner(1)
        i  = 0
        while i < 1000:  
            rollNumber = testGameRunner.rollDice()
            #print("roll number: "+ str(rollNumber))
            self.assertTrue(rollNumber in range(0,13))
            i += 1
#Randon line
unittest.main()