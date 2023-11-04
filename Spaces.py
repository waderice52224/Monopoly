class Space:
    def __init__(self, name, val, cost=0):
        self.name = name
        self.spaceVal = val
        self.cost = cost

    def getBoardVal(self):
        return self.spaceVal

    def getNameOfSpace(self):
        return self.name
    def getCost(self):
        return self.cost