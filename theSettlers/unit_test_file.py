import unittest
from player import Player
from card_types import ResCard,DevCard
from run_game import GameRunner
from node_object import NodeObject

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
        #print("Number of hexagons:"+ str(len(testGameRunner.hexagons)))
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
#This test class would fit the convention better as just a series of tests
#within the gameRunner but the naming system needed would be more complex than
#necessary
class testBuildRoad(unittest.TestCase):
    #Currently using print statments as the output so hard to test
    #If code changes need to update these unit tests
    def testSameNodePassed(self):
        testNode1 = NodeObject(1)
        testGameRunner = GameRunner(1)
        testGameRunner.buildRoad(testNode1, testNode1, 0)
        
    def testRoadAlreadyExist(self):
        testNode1 = NodeObject(1)
        testNode2 = NodeObject(2)
        testGameRunner = GameRunner(1)
        testGameRunner.roads.append([testNode1, testNode2])
        testGameRunner.buildRoad(testNode1, testNode2, 0)

    def testRoadNeedsConnectingRoad(self):
        testNode1 = NodeObject(1)
        testNode2 = NodeObject(2)
        testGameRunner = GameRunner(1)
        testGameRunner.buildRoad(testNode1, testNode2, 0)

    def testBuildRoad(self):
        testNode1 = NodeObject(1)
        testNode2 = NodeObject(2)
        testNode3 = NodeObject(3)
        testGameRunner = GameRunner(1)
        testGameRunner.players[0].playerRoads.append(testNode2)
        testGameRunner.players[0].playerRoads.append(testNode3)
        testGameRunner.roads.append([testNode2, testNode3])
        testGameRunner.buildRoad(testNode1, testNode2, 0)
unittest.main()