from theSettlers.cardTypes import ResCard,DevCard

# The Class for the player
class Player:
    def __init__ (self, game, num):
        # the game the player belongs to
        self.game = game
        # the player number for this player
        self.num = num
        # the number of victory points
        self.victory_points = 0
        # List holding the resource cards the player has from the Enum 'cardTypes'
        self.resCards = []
        # List holding the development cards the player has from the Enum 'cardTypes'
        self.developCards = []
        # the longest road segment this player has
        self.longest_road_length = 0

    # Adds any amount of cards to the players card deck
    def addCards(self, cards):
        # Loops through each card thats given
        for card in cards:
            self.resCards.append(card)

    # Removes any amount of cards from the players card deck
    def removeCards(self, cards):
        # Loops through each card thats given
        for card in cards:
            # Finds index of specific card in the players deck and deletes that card from the players deck
            del self.cards[self.cards.index(card)]
    
    # Checks to see if the given cards are in the players deck
    def has_cards(self, cards):

        # Will duplicate the cards to effectively check if needed cards
        # are in the players deck
        cardsDuplicate = self.cards[:]

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

    # Removes a development card from the players deck
    def removeDevelopCard(self, card):
        # Finds the index of the card in the players deck and deletes it from the players deck
        del self.developCards[self.developCards.index(card)]

    # Checks if a specific development card is in a players deck
    def has_dev_cards(self, card):
        if self.developCards.__contains__(card):
            return True
        else:
            return False

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
        

