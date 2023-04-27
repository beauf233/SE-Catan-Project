import unittest
from player import Player
from card_types import ResCard,DevCard
from run_game import GameRunner
from node_object import NodeObject


class testPlayerClass(unittest.TestCase):
    """
    In this test class the methods within the Player class are being tested,
    the Player classes main role in the structure of the game is to hold the 
    cards that the player has at their disposal.

    Methods that are written below:
    :testAddRemoveHasResCard - tests the methods related to resCards
    :testAddHasRemoveDevCard - tests the methods related to devCards
    """

    def testAddRemoveHasResCard(self):
        """
        Tests the functionality of the player objects resCard related methods,
        
        The methods tested include:
        :addResCards
        :hasResCards
        :removeResCards
        """

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
    
    def testAddHasRemoveDevCard(self):
        """
        Tests the functionality of the player object devCard related methods
        
        Tests the methods:
        :addDevCard
        :hasDevCards
        :removeDevCard
        """

        currentGame = GameRunner(1)
        testDevCard = DevCard(1)
        testPlayer = Player(currentGame, 1)
        #listOfCards = [testDevCard]
        testPlayer.addDevCard(testDevCard)
        self.assertEqual(testPlayer.hasDevCards(testDevCard), True, "card not present")
        testDevCard2 = DevCard(2)
        testPlayer.removeDevCard(testDevCard)
        testPlayer.addDevCard(testDevCard2)
        #listOfCards.append(testDevCard2)
        self.assertEqual(testPlayer.hasDevCards(testDevCard), False)

class testRunGame(unittest.TestCase):
    """
    In this class the methods within the GameRunner class are being tested, 
    these tests will prove that the operability of the methods is as expected
    
    Methods that are written below:
    :testShuffleDevelopDeck - tests developDeck setup
    :testPlayerPickUpDevCard - tests player picking up devCard
    :testInnitHexagons - tests hexagon intialisation
    :testRollDice - tests that the dice are rolling correctly
    """

    def testShuffleDevelopDeck(self):
        """
        Tests the shuffleDevelopCards method of the GameRunner, which is used in the intialiser
        to set-up the developDeck attribute. This method is simply checked to make sure the deck is 25
        indices long which indicates that there are the correct number of cards present
        
        Methods tested are:
        :shuffleDevelopDeck
        """

        testGameRunner = GameRunner(3)
        testDevelopCardDeck = testGameRunner.shuffleDevelopCards()
        self.assertEqual(len(testDevelopCardDeck), 25)
    
    
    def testPlayerPickUpDevCard(self):
        """
        Tests the pickUpDevCard method within the gameRunner, this is important as it is calling the method
        of an intiated object within itself, so it is important to make sure it runs as it should.
        
        Methods that are tested:
        :pickUpDecCard
        :getPlayer
        """

        testGameRunner = GameRunner(2)
        testDevCard = testGameRunner.developDeck[24]
        testGameRunner.pickUpDevCard(0)
        testPlayer = testGameRunner.getPlayer(0)
        self.assertEqual(testPlayer.hasDevCards(testDevCard), True)

    
    def testInnitHexagons(self):
        """
        Tests that the hexagons are intiated properly
        
        Methods that are tested:
        :innitHexagons
        """

        testGameRunner = GameRunner(1)
        self.assertEqual(len(testGameRunner.hexagons), 19)
    
    def testRollDice(self):
        """
        Tests the roll dice method by running the function 1000 times and checking
        that the summed result is within the expected guidelines
        
        Methods tested:
        :rollDice
        """

        testGameRunner = GameRunner(1)
        i  = 0
        while i < 1000:  
            rollNumber = testGameRunner.rollDice()
            #print("rolled number: "+ str(rollNumber))
            self.assertTrue(rollNumber in range(2,13))
            i += 1

class testcanBuildRoad(unittest.TestCase):
    """
    This test class is an extenstion of the testGameRunner class above, a seperate test
    class was used as the importance of the GameRunner.canBuildRoad method was deemed important
    and complex enough to warrant it's own class of tests
    
    Test methods used are:
    :testSameNodePassed - tests the error that user passed same two nodes
    :testRoadAlreadyExist - tests to see if specific road already exists
    :testRoadNeedsConnectingRoad - tests to see if there is a connection point for new road
    :testcanBuildRoad - tests to see if road can be built given correct conditions

    Note: the code currently uses print statements in the GameRunner class, so no assertEquals statments yet
    """

    def setUp(self):
        self.testGameRunner = GameRunner(1)
        self.testNode1 = NodeObject(1)
        self.testNode2 = NodeObject(2)
        self.testNode3 = NodeObject(3)
        self.cardsNeeded = [
            ResCard.Wood,
            ResCard.Brick
        ]
        self.testGameRunner.players[0].addResCards(self.cardsNeeded)

    def tearDown(self):
        self.testGameRunner = None
        self.testNode1 = None
        self.testNode2 = None
        self.testNode3 = None

    def testHasResCard(self):
        print("\nOutput should be: 'You do not have the needed resources cards to make this'")
        self.testGameRunner.players[0].removeResCards(self.cardsNeeded)
        self.testGameRunner.canBuildRoad(self.testNode1, self.testNode1, 0)

    def testSameNodePassed(self):
        """
        Tests to see if the two nodes that are passed to the canBuildRoad method are in fact that same
        node, this will be useful if the user clicks the same node by accident
        
        Methods that are tested:
        :canBuildRoad
        """

        print("\nOutput should be: 'You have to choose different nodes to build a road'")
        self.testGameRunner.players[0].addResCards(self.cardsNeeded)
        self.testGameRunner.canBuildRoad(self.testNode1, self.testNode1, 0)
        
    def testRoadAlreadyExist(self):
        """
        Tests to see if a road already exists between these two nodes, this will be good for game 
        function as it will mean the player does not have the ability to waste resources by accident
        by placing a new road on a pre-existing road

        Methods that are tested:
        :canBuildRoad
        """

        print("\nOutput should be: 'There is already a road here'")
        self.testGameRunner.roads.append([self.testNode1, self.testNode2])
        self.testGameRunner.canBuildRoad(self.testNode1, self.testNode2, 0)

    def testRoadNeedsConnectingRoad(self):
        """
        Tests to see if the road that is being built will have another road to connect to, this is crucial
        as a road cannot simply be built anywhere otherwise this would mess with the game tactics and disrupt
        other players building decisions. 

        Methods that are tested:
        :canBuildRoad
        """

        print("\nOutput should be: 'You need to have a connecting road to build a road here'")
        self.testGameRunner.canBuildRoad(self.testNode1, self.testNode2, 0)

    def testcanBuildRoad(self):
        """
        Tests the overall functionality, within this scenario the set-up is such that the game should
        be able to build a road as there is a pre-existing road already added in which to connect to and 
        the nodes passed to the function are in themselves unique
        
        Methods that are tested:
        :canBuildRoad
        """

        print("\nOutput should be: 'Road is being built'")
        self.testGameRunner.players[0].playerRoads.append(self.testNode2)
        self.testGameRunner.players[0].playerRoads.append(self.testNode3)
        self.testGameRunner.roads.append([self.testNode2, self.testNode3])
        self.testGameRunner.canBuildRoad(self.testNode1, self.testNode2, 0)

class testCanBuildSettlement(unittest.TestCase):
    """
    This test class is another extension of the testGamerRunner class, it is seperated as there is a 4 
    conditional branch where the player receives feedback on whether they are able to build a settlement 
    in a desired place. As with the build road method, the canBuildSettlement method also uses print 
    statements for displayers errors, so manual checking of print statements will be necessary
    
    Test methods used are:
    :testNeedResourcesForSettlement - Tests if player has required resCards
    :testAlreadySettlment - Tests if a settlement already exists on selected node
    :testCanBuildSettlementTrueCase - Tests, given correct conditions, that a settlement is built
    """

    def setUp(self):
        self.testGameRunner = GameRunner(1)
        self.cardsNeeded = [
            ResCard.Wood,
            ResCard.Brick,
            ResCard.Sheep,
            ResCard.Wheat
        ]

    def testNeedResourcesForSettlement(self):
        """
        This method tests whether the player has enough resources required to build a settlement, and if they
        do not then that the appropriate error message is displayed.

        Methods tested:
        :canBuildSettlement
        """
        print("\nOutput should be: 'You do not have the needed resources cards to make this'")
        self.testGameRunner.canBuildSettlement(self.testGameRunner.nodes[0], 0)

    def testAlreadySettlment(self):
        """
        This method tests whether the GameRunner class will be able to filter out when a player tries to build
        a settlement on a node that already contains a settlement. This will be paramount to ensuring as few 
        bugs as possible. 

        Methods tested:
        :canBuildSettlement
        """

        self.testGameRunner.buildSettlement(self.testGameRunner.nodes[0], 0)
        self.testGameRunner.players[0].addResCards(self.cardsNeeded)
        print("\nOutput should be: 'There is already a settlement built here'")
        self.testGameRunner.canBuildSettlement(self.testGameRunner.nodes[0], 0)

    def testCanBuildSettlementTrueCase(self):
        """
        Tests the true case when the player should be able to build a settlement, this requires the player
        to have chosen a node that is atleast two nodes path from the nearest settlement, and also to have
        the correct resources needed. Additionally, a settlement cannot already be on this node.

        Methods tested:
        :canBuildSettlement
        :buildSettlment
        """

        self.testGameRunner.players[0].addResCards(self.cardsNeeded)
        print("\nOutput should be: 'Settlement is being built'")
        self.testGameRunner.canBuildSettlement(self.testGameRunner.nodes[0], 0)
        self.testGameRunner.players[0].addResCards(self.cardsNeeded)
        print("\nOutput should be: 'There is already a settlement built here'")
        self.testGameRunner.canBuildSettlement(self.testGameRunner.nodes[0], 0)
unittest.main()