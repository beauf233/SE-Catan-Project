from player import Player
from cardTypes import DevCard, ResCard
from hexValues import hexType
from hexagonObject import HexagonObject
import random 

class GameRunner:
    def __init__(self, numPlayers):

        self.players = []
        for i in range(numPlayers):
            self.players.append(Player(game=self, num=i)) 
        print('fin')
        self.developDeck = self.shuffleDevelopCards()
        self.hexagons = self.innitHexagons()        

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
    
    def innitHexagons():
        hexagons = []

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
                    hexagons.append(HexagonObject(i, hexType.Desert, 4))
                    Desert -= 1
                    if Desert == 0:
                        del myNumbers[myNumbers.index(0)]
                case 1:
                    hexagons.append(HexagonObject(i, hexType.Mountain, 4))
                    Mountains -= 1
                    if Mountains == 0:                        
                        del myNumbers[myNumbers.index(1)]
                case 2:
                    hexagons.append(HexagonObject(i, hexType.Hill, 4))
                    Hills -= 1
                    if Hills == 0:                        
                        del myNumbers[myNumbers.index(2)]
                case 3:
                    hexagons.append(HexagonObject(i, hexType.Field, 4))
                    Fields -= 1
                    if Fields == 0:                        
                        del myNumbers[myNumbers.index(3)]
                case 4:
                    hexagons.append(HexagonObject(i, hexType.Pasture, 4))
                    Pasture -= 1
                    if Pasture == 0:                        
                        del myNumbers[myNumbers.index(4)]
                case 5:
                    hexagons.append(HexagonObject(i, hexType.Forest, 4))
                    Forest -= 1
                    if Forest == 0:
                        del myNumbers[myNumbers.index(5)]
            
            return hexagons
