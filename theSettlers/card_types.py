from enum import Enum

# The different types of resource cards
class ResCard(Enum):

    # the resource cards
    Wood = 0
    Brick = 1
    Ore = 2
    Sheep = 3
    Wheat = 4

# The different types of developement cards
class DevCard(Enum):

    # the developement cards
    VictoryPoint = 0
    Knight = 1
    RoadBuilding = 2
    YearOfPlenty = 3
    Monopoly = 4