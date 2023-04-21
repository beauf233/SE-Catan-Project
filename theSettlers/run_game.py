from player import Player
from card_types import DevCard, ResCard
from hex_values import hexType
from hexagon_object import HexagonObject
from node_object import NodeObject
import random 

class GameRunner:
    """
    This class is designed to hold all the information pertinent to a specific instance 
    of a game. This will involve holding all of the players that are in the game, and also  
    storing the information related to the hexagons and their intialisation as well. This class
    is able to add as many players as specified to the game

    Attributes:
    :players - A list containing all the player objects
    :nodes - A list containing all the nodes which will be related to the hexagons
    :roads - A list that contains all the roads made in the game
    :hexRelationships - A list containing lists which themselves contain numbers relating to how the
    nodes will relate to the hexagons
    :developDeck - A list containing 25 shuffled development cards
    :hexagons - A list containing all the hexagon objects
    """

    def __init__(self, numPlayers):
        """
        Parameters:
        :numPlayers - The number of players in this game instance
        """
        self.players = []
        self.nodes = []
        self.roads = []
        self.settlements = []
        hexRelationships =[[0, 3, 4, 7, 8, 12], [1, 4, 5, 8, 9, 13], [2, 5, 6, 9, 10, 14], [7, 11, 12, 16, 17, 22], [8, 12, 13, 17, 18, 23], [9, 13, 14, 18, 19, 24], [10, 14, 15, 19, 20, 25], [16, 21, 22, 27, 28, 33], [17, 22, 23, 28, 29, 34], [18, 23, 24, 29, 30, 35], [19, 24, 25, 30, 31, 36], [20, 25, 26, 31, 32, 37], [28, 33, 34, 38, 39, 43], [29, 34, 35, 39, 40, 44], [30, 35, 36, 40, 41, 45], [31, 36, 37, 41, 42, 46], [39, 43, 44, 47, 48, 51], [40, 44, 45, 48, 49, 52], [41, 45, 46, 49, 50, 53]]
        for i in range(numPlayers):
            self.players.append(Player(game=self, num=i)) 
            #print(self.players[i])
        for i in range(0,53):
            self.nodes.append(NodeObject(i))

        #print('Test GameRunner intiated')
        self.developDeck = self.shuffleDevelopCards()
        self.innitHexagons(hexRelationships)

    def getPlayer(self, chosePlayer):
        """
        Simple accessor method created in order to retrieve the specific player 
        which is identified using the chosePlayer parameter

        Parameters:
        :chosePlayer - Int used to identify the desired player from the list
        """

        return self.players[chosePlayer]

    def shuffleDevelopCards(self):
        """
        This method is designed to return a list that contains a randomised order of devCards,
        this will be used when a player wants to purchase a devCard as it means the game can simply 
        pop a card off the end of the list and give it to the player who will then add it to their
        list of devCards. The number of cards in the deck will be 25.
        """

        developDeck = []

        # Numbers of each cards present in the game
        # There are 25 total
        knightCards = 14
        victoryPointCards = 5
        roadBuilding = 2
        yearOfPlenty = 2
        monopoly = 2

        myNumbers = [0,1,2,3,4]

        # Iterate and randomly select cards until there are no cards remaining
        while knightCards + victoryPointCards + roadBuilding + yearOfPlenty + monopoly != 0:
            
            pick = random.choice(myNumbers)
            
            match pick:
                case 0:
                    developDeck.append(DevCard.Knight)
                    knightCards -= 1
                    if knightCards == 0:
                        del myNumbers[myNumbers.index(0)]
                case 1:
                    developDeck.append(DevCard.VictoryPoint)
                    victoryPointCards -= 1
                    if victoryPointCards == 0:
                        del myNumbers[myNumbers.index(1)]
                case 2:
                    developDeck.append(DevCard.RoadBuilding)
                    roadBuilding -= 1
                    if roadBuilding == 0:
                        del myNumbers[myNumbers.index(2)]
                case 3:
                    developDeck.append(DevCard.YearOfPlenty)
                    yearOfPlenty -= 1
                    if yearOfPlenty == 0:
                        del myNumbers[myNumbers.index(3)]
                case 4:
                    developDeck.append(DevCard.Monopoly)
                    monopoly -= 1
                    if monopoly == 0:
                        del myNumbers[myNumbers.index(4)]
        return developDeck
    
    def displayDevelopDeck(self):
        """
        This method is used to display the developDeck. This was necessary so that during testing it was
        easy to see that the developDeck had been randomised and not just the same order of cards added.
        """

        for devCard in self.developDeck:
            print(devCard)

    def pickUpDevCard(self, i):
        """
        This mutator method is used so that from within the GameRunner object it is possible to add devCards
        to a specific player
        """

        self.players[i].addDevCard(self.developDeck.pop())

    #Method used to make a development card
    #Method needs to change the develop card
    def buildDevelopCard(self, builderPlayer):
        """
        This method is to be used by the player in the event they attempt to purchase a development 
        card. It does this by creating a list of cards that are needed, which it then passes to the
        player object via the hasResCards method that will determine if the player has the required 
        cards for the transaction. If the player does have the resCards needed then a devCard will 
        be picked up from the developDeck.

        Parameters:
        :i - The identifier for the player
        """

        cardsNeeded = [
            ResCard.Sheep,
            ResCard.Wheat,
            ResCard.Ore
        ]

        if not self.players[builderPlayer].hasResCards(cardsNeeded):
            print("You do not have the needed resources cards to make this")
        else:
            self.pickUpDevCard(builderPlayer)
    
    def innitHexagons(self, hexRelationships):
        """
        This method is used to create a randomised list of hexagons that are to be used in the board.
        This randomised list will contain the same 19 hexagons, just in a random order. The hexagons 
        will be intialised with the value in hexRelationships that it corresponds to. i.e whatever 
        hexagon is chosen first will have the set of hexRelaationships found at index 0, the second 
        hexagon index 1 etc.

        Parameters:
        :hexRelationships - A list containing lists of all the integer nodes that correspond to each 
        hexagon. These will be fundamental in allowing roads and settlements to be built properly
        """

        self.hexagons = []

        # Number of certain tile type on the board
        desert = 1
        mountain = 3
        hill = 3
        field = 4
        pasture = 4
        forest = 4

        myNumbers = [0,1,2,3,4,5]

        while desert + mountain + hill + field + pasture + forest != 0:
            
            pick = random.choice(myNumbers)
            i = 19 - (desert + mountain + hill + field + pasture + forest)

            match pick:
                case 0:
                    self.hexagons.append(HexagonObject(i, hexType.Desert, hexRelationships[i]))
                    desert -= 1
                    if desert == 0:
                        del myNumbers[myNumbers.index(0)]
                case 1:
                    self.hexagons.append(HexagonObject(i, hexType.Mountain, hexRelationships[i]))
                    mountain -= 1
                    if mountain == 0:                        
                        del myNumbers[myNumbers.index(1)]
                case 2:
                    self.hexagons.append(HexagonObject(i, hexType.Hill, hexRelationships[i]))
                    hill -= 1
                    if hill == 0:                        
                        del myNumbers[myNumbers.index(2)]
                case 3:
                    self.hexagons.append(HexagonObject(i, hexType.Field, hexRelationships[i]))
                    field -= 1
                    if field == 0:                        
                        del myNumbers[myNumbers.index(3)]
                case 4:
                    self.hexagons.append(HexagonObject(i, hexType.Pasture, hexRelationships[i]))
                    pasture -= 1
                    if pasture == 0:                        
                        del myNumbers[myNumbers.index(4)]
                case 5:
                    self.hexagons.append(HexagonObject(i, hexType.Forest, hexRelationships[i]))
                    forest -= 1
                    if forest == 0:
                        del myNumbers[myNumbers.index(5)]
    
    #Generates 2 seperate integer values to simulate a random dice roll
    #Results are summed and the value returned
    def rollDice(self):
        """
        This method is the backend for a dice roll. It choses two random integer values between 1 and 6
        and then sums the result. This result is the value the player uses for their turn
        """

        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        combRoll = roll1+roll2
        #print(combRoll)
        if combRoll == 7:
            self.moveRobber()

        #for i in range(0,5):
        #    self.nodes[ self.hexagons[4].giveNodes(5) ]
        
        return combRoll

    def canBuildRoad(self, node1, node2, builderPlayer):
        """
        This method is used to check that a road can be built by a particular player at two given nodes. There
        is a conditional statement throughout this method that is checking the applicability of a given players 
        choice of two nodes. This is crucial as the placement of roads is an important component in tactics 
        within the Settlers

        Parameters:
        :node1 - The first node in the road that is beind tested
        :node2 - The second node in the road that is beind tested
        :builderPlayer - The identifier for the player attempting to build the road
        """
        cardsNeeded = [
            ResCard.Wood,
            ResCard.Brick
        ]

        if not self.players[builderPlayer].hasResCards(cardsNeeded):
            print("You do not have the needed resources cards to make this")
        elif node1 == node2:
            print("You have to choose different nodes to build a road")
        elif self.roads.__contains__([node1,node2]):
            print("There is already a road here")
        elif not (self.players[builderPlayer].playerRoads.__contains__(node1) or self.players[builderPlayer].playerRoads.__contains__(node2)):
            print("You need to have a connecting road to build a road here")
        else:
            print("Road is being built")
            self.buildRoad(node1, node2, builderPlayer)
    
    def buildRoad(self, node1, node2, builderPlayer):
        self.roads.append([node1,node2])
        self.players[builderPlayer].playerRoads.append([node1,node2])

    def twoIntersectionsAway(self, node):      
        # TO DO
        # indexof in array of hexagons and find pattern
        return True

    def canBuildSettlement(self, node, builderPlayer):
        
        cardsNeeded = [
            ResCard.Wood,
            ResCard.Brick,
            ResCard.Sheep,
            ResCard.Wheat
        ]

        if not self.players[builderPlayer].hasResCards(cardsNeeded):
            print("You do not have the needed resources cards to make this")
        elif self.settlements.__contains__(node):
            print("There is already a settlement built here")
        elif not(self.twoIntersectionsAway(node)):
            print("A settlement can only be built two intersectios away from a settlement or city")
        else:
            print("Settlement is being built")
            self.buildSettlement(node, builderPlayer)

    def buildSettlement(self, node, builderPlayer):
        self.settlements.append(node)
        self.players[builderPlayer].playerSettlements.append(node)

    def moveRobber():
        print