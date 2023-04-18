
class HexagonObject:
    """
    This class is used to represent the hexagon objects used in the game

    Attributes:
    :hexNumber - The numerical identifier for a given hexagon object
    :hexagonType - The type of hexagon determined by it's given Enum
    :nodeRelationship - The set of nodes that are related to a given hexagon object
    """

    def __init__(self, number, hexagonType, relationship):
        """
        Parameters:
        :number - The identifier assigned to the hexagon instance
        :hexagonType - The enum determined type of the hexagon
        :relationship - The set of nodes that are to be related to the hexaogn
        """

        self.hexNumber = number
        self.hexagonType = hexagonType
        self.nodeRelationship = relationship

    def giveNodes(self):
        """
        This is a simple accessor method used in order to determine which nodes 
        are related to a given hexagon.
        """
        return self.nodeRelationship
                    