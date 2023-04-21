from card_types import ResCard,DevCard

class Player:
    """
    This class is designed to be the class that holds the information pertinent to each individual player,
    it shall store the information for the resCards and devCards that the player posesses. As well as this,
    each player will store their own scores as far as victory points and longest road achievements etc. These
    will be accessible from other classes and will be used by other methods
    
    Attributes:
    :game - The game the player belongs to
    :playerNum - The players number
    :victory_points - The num of victory points the player has
    :resCards - List holding the resource cards the player has from the Enum 'cardTypes'
    :developCards - List holding the development cards the player has from the Enum 'cardTypes'
    :longest_road_length - The length of the longest road segment a player has
    :playerRoads - The list of roads the player has
    """

    def __init__ (self, game, num):
        """
        Parameters:
        :game - The game that the player will be apart of
        :num - The value that is used to identify each player (playerNum)
        """
        
        self.game = game
        self.playerNum = num
        self.victory_points = 0
        self.longest_road_length = 0
        self.resCards = []
        self.developCards = []
        self.playerRoads = []
        self.playerSettlements = []
    
    def addResCards(self, cards):
        """
        In this method there will be a list of resCards passed to it, and will then be added
        to a players resCard deck. This will be used when the game rolls a dice and resource 
        cards are distrbuted

        Parameters:
        :cards - A list of resCards that will be added to the players resCard list
        """
        
        # Loops through each card thats given
        for card in cards:
            if isinstance(card, ResCard):
                self.resCards.append(card)
            else:
                print("That was not a Rescard")

    def removeResCards(self, cards):
        """
        This method will remove as many cards as passed to it from the players resCard list.
        This will be used when the player either loses cards due to a game function, or when they
        are purchasing a building or card

        Parameters:
        :cards - A list of resCards that will be removed from the players resCard list
        """
        # Loops through each card thats given
        for card in cards:
            # Finds index of specific card in the players deck and deletes that card from the players deck
            del self.resCards[self.resCards.index(card)]
    
    def hasResCards(self, cards):
        """
        Checks the players resCards list to see if it contains the complete set of cards that are
        passed to the method. The method will only return true if every single card that is passed is
        present within the players resCard list. It takes into account any cards there are multiple of
        within the passed cards list and checks for the correct number of the cards in the resCards list

        Parameters:
        :cards - The cards to be removed from the resCards list
        """

        # Will duplicate the cards to effectively check if needed cards
        # are in the players deck. This will be used to check for correct
        # numbers of each card
        cardsDuplicate = self.resCards[:]

        for card in cards:
            # Checks the number of times the card appears in the list
            # if it is 0 that means the card thats being searched for
            # isn't in the players deck and will return false
            if cardsDuplicate.count(card) == 0:
                return False
            else:
                # Removes the card from the duplicate list as that
                # card cannot be counted anymore
                del cardsDuplicate[cardsDuplicate.index(card)]

        # As the loop has been completed that means all cards were found in the deck
        return True
    
    def addDevCard(self, devCard):
        """
        Adds a singular devCard to the players developCards list

        Parameters:
        :devCard - The development card that is to be added
        """
        self.developCards.append(devCard)
    
    def removeDevCard(self, devCard):
        """
        Removes a singular devCard from the developCards list

        Parameters:
        :devCard - The development card that is to be removed
        """
        del self.developCards[self.developCards.index(devCard)]

    def hasDevCards(self, devCard):
        """
        Checks to see if a singular devCard is in the developCards list of the given player
        object

        Parameters:
        :devCard - The development card to be checked for its presence in the developCards list
        """
        return self.developCards.__contains__(devCard)
        
    def updateLongestRoad(self):
        currentLongestRoad = 0
        currentNode = 0

        for settlementNode in self.playerSettlements:
            for i in range(0,len(self.playerRoads)):
                for j in range(0,1):
                    if settlementNode == self.playerRoads[i,j]:
                        match j:
                            case 0:
                                self.again(self.playerRoads[i,1])
                            case 1:
                                self.again(self.playerRoads[i,0])
            
    def again(self, node):
        if self.playerRoads.__contains__(node):
            self.playerRoads.index(node)
            return self.again(node)
        else:
            return 1
    
    def findRoadSegements(self):
        roadSet = []
        while all == True:
            for i in range(0, len(self.playerRoads))