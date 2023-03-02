
class HexagonObject:

    def __init__(self, number, hexagonType, relationship):
        self.hexNumber = number
        self.hexagonType = hexagonType
        self.nodeRelationship = relationship

    def giveNodes(self):
        return self.nodeRelationship
                    