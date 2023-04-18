from enum import Enum

class ResCard(Enum):
    """
    An Enum class used to represent each of the available resource cards
    """

    # the resource cards
    Wood = 0
    Brick = 1
    Ore = 2
    Sheep = 3
    Wheat = 4

class DevCard(Enum):
    """
    An Enum class used to represent each of the available development cards
    """

    # the developement cards
    VictoryPoint = 0
    Knight = 1
    RoadBuilding = 2
    YearOfPlenty = 3
    Monopoly = 4