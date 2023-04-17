from card_types import ResCard,DevCard

# The Class for the player
class Player:
    def __init__ (self, game, num):
        # the game the player belongs to
        self.game = game
        # the player number for this player
        self.playerNum = num
        # the number of victory points
        self.victory_points = 0
        # List holding the resource cards the player has from the Enum 'cardTypes'
        self.resCards = []
        # List holding the development cards the player has from the Enum 'cardTypes'
        self.developCards = []
        # The longest road segment this player has
        self.longest_road_length = 0
        # List holding the roads the player has built
        self.playerRoads = []
    
    # Adds any amount of cards to the players card deck
    def addResCards(self, cards):
        # Loops through each card thats given
        for card in cards:
            #print(card)
            #Simplest check to make sure the card is correct type
            #Won't be used by the user but will be helpful for debugging
            if isinstance(card, ResCard):
                self.resCards.append(card)
            #Only useful if needing to break from the loop
            #else:
            #    print("That was not a Rescard")

    # Removes any amount of cards from the players card deck
    def removeResCards(self, cards):
        # Loops through each card thats given
        for card in cards:
            # Finds index of specific card in the players deck and deletes that card from the players deck
            del self.resCards[self.resCards.index(card)]
    
    # Checks to see if the given cards are in the players deck
    def hasResCards(self, cards):

        # Will duplicate the cards to effectively check if needed cards
        # are in the players deck
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
    
    # Adds the development card to the players development card deck
    def addDevCard(self, devCard):
        self.developCards.append(devCard)
        #print("Test addDevCard")

    # Removes a development card from the players deck
    def removeDevCard(self, card):
        # Finds the index of the card in the players deck and deletes it from the players deck
        del self.developCards[self.developCards.index(card)]

    # Checks if a specific development card is in a players deck
    def hasDevCards(self, card):
        #if self.developCards.__contains__(card):
        #    return True
        #else:
        #    return False
        return self.developCards.__contains__(card)

    def buildSettlement(self, corner):
        # The needed resources the player will need to build a settlement
        cards_needed = [
            ResCard.Wood,
            ResCard.Brick,
            ResCard.Sheep,
            ResCard.Wheat
        ]

        # Checks to see if the needed cards are in the players deck
        if not self.has_cards(cards_needed):
            print("not enough of the right cards") ######## FIX #######
            return None
        
    