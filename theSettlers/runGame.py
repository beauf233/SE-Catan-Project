from player import Player
from cardTypes import DevCard, ResCard
from hexValues import hexType
from hexagonObject import HexagonObject
from nodeObject import NodeObject
import random 

class GameRunner:

    def __init__(self, numPlayers):

        self.players = []
        hexRelationships =[[0, 3, 4, 7, 8, 12], [1, 4, 5, 8, 9, 13], [2, 5, 6, 9, 10, 14], [7, 11, 12, 16, 17, 22], [8, 12, 13, 17, 18, 23], [9, 13, 14, 18, 19, 24], [10, 14, 15, 19, 20, 25], [16, 21, 22, 27, 28, 33], [17, 22, 23, 28, 29, 34], [18, 23, 24, 29, 30, 35], [19, 24, 25, 30, 31, 36], [20, 25, 26, 31, 32, 37], [28, 33, 34, 38, 39, 43], [29, 34, 35, 39, 40, 44], [30, 35, 36, 40, 41, 45], [31, 36, 37, 41, 42, 46], [39, 43, 44, 47, 48, 51], [40, 44, 45, 48, 49, 52], [41, 45, 46, 49, 50, 53]]
        for i in range(numPlayers):
            self.players.append(Player(game=self, num=i)) 

        for i in range(0,53):
            self.nodes.append(NodeObject(i))

        print('fin')
        self.developDeck = self.shuffleDevelopCards()
        self.innitHexagons(hexRelationships)

    def shuffleDevelopCards():
        developDeck = []


        # Numbers of each cards present in the game
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
    

    def pickUpCard(self, i):
        self.players[i].addDevCard(self.developDeck.pop())

    def buildDevelopCard(self, i):
        cardsNeeded = [
            ResCard.Sheep,
            ResCard.Wheat,
            ResCard.Ore
        ]

        if not self.players[i].has_cards(cardsNeeded):
            return None
        else:
            self.players[i].pickUpCard(i)
    
    def innitHexagons(self, hexRelationships):
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
                    Desert -= 1
                    if Desert == 0:
                        del myNumbers[myNumbers.index(0)]
                case 1:
                    self.hexagons.append(HexagonObject(i, hexType.Mountain, hexRelationships[i]))
                    Mountains -= 1
                    if Mountains == 0:                        
                        del myNumbers[myNumbers.index(1)]
                case 2:
                    self.hexagons.append(HexagonObject(i, hexType.Hill, hexRelationships[i]))
                    Hills -= 1
                    if Hills == 0:                        
                        del myNumbers[myNumbers.index(2)]
                case 3:
                    self.hexagons.append(HexagonObject(i, hexType.Field, hexRelationships[i]))
                    Fields -= 1
                    if Fields == 0:                        
                        del myNumbers[myNumbers.index(3)]
                case 4:
                    self.hexagons.append(HexagonObject(i, hexType.Pasture, hexRelationships[i]))
                    Pasture -= 1
                    if Pasture == 0:                        
                        del myNumbers[myNumbers.index(4)]
                case 5:
                    self.hexagons.append(HexagonObject(i, hexType.Forest, hexRelationships[i]))
                    Forest -= 1
                    if Forest == 0:
                        del myNumbers[myNumbers.index(5)]
            
            #return hexagons
    
    def rollDice(self):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        combRoll = roll1+roll2

        for i in range(0,5):
            self.nodes[ self.hexagons[4].giveNodes(5) ]