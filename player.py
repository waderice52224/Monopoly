import random
class Player:
    def __init__(self, playerName, position, money, properties):
        self.playerName = playerName
        self.position = position
        self.money = money
        self.properties = properties

    def rollDice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        totalDice = dice2 + dice1
        self.position += totalDice
        if self.position > 40:
            self.position = self.position - 40

    def getName(self):
        return self.playerName

    def getPosistion(self):
        return self.position

    def getMoney(self):
        return self.money

    def getProperties(self):
        return self.properties

    def buyProperty(self, property, cost):
        self.properties.append(property)
        self.money = self.money - cost
        property.purchase()


