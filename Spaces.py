class Space:
    def __init__(self, name, val, typeSpace, cost=0):
        self.name = name
        self.spaceVal = val
        self.typeSpace = typeSpace
        self.cost = cost

    def getBoardVal(self):
        return self.spaceVal

    def getNameOfSpace(self):
        return self.name
    def getCost(self):
        return self.cost

    def canbuy(self):
        return False

    def getType(self):
        return self.typeSpace


#all types of Properties
# 0 = Houseable
# 1 = Railroad
# 2 = Util
# 3 = Jail
# 4 = Just visit
# 5 = Free Parking
# 6 = Go
# 7 = ComChest
# 8 = Chance