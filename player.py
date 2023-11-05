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
        if dice2 == dice1:
            print("TODO")
            #rolled doubles, player gets out of jail and/or gets another turn
        totalDice = dice2 + dice1
        self.position += totalDice
        if self.position >= 40:
            self.money += 200
            self.position = self.position - 40
            if self.position == 0:
                self.position = 40


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

    def checkSpace(self, property):
        if property.getType() == 0:
            Player.landedHousble(self, property)
        elif property.getType() == 1:
            Player.landedRailroad(self, property)
        elif property.getType() == 2:
            Player.landedUtil(self, property)
        elif property.getType() == 3:
            Player.landedJail(self)
        elif property.getType() == 4:
            Player.landedJustVisiting(self)
        elif property.getType() == 5:
            Player.landedFreeParking(self)
        elif property.getType() == 6:
            Player.landedGo(self)
        elif property.getType() == 7:
            #Player.playerLandedComChest(self, Cc2)
            print("FIXME")
        elif property.getType() == 8:
            #Player.playerLandedChance(self, c10)
            print("FIXME")
        elif property.getType() == 9:
            Player.playerLandedTaxes(self, property)

    def landedHousble(self, property):
        if property.canbuy():
            # Player Makes Decision on purchase
            # For now if player can afford it will buy
            if (self.money - property.getCost()) >= 0:
                Player.buyProperty(self, property, property.getCost())
        else:
            print("TODO")
            #payRent


    def landedRailroad(self, property):
        if property.canbuy():
            # Player Makes Decision on purchase
            # For now if player can afford it will buy
            if (self.money - property.getCost()) >= 0:
                Player.buyProperty(self, property, property.getCost())
        else:
            print("TODO")
            #payRent

    def landedUtil(self, property):
        if property.canbuy():
            # Player Makes Decision on purchase
            # For now if player can afford it will buy
            if (self.money - property.getCost()) >= 0:
                Player.buyProperty(self, property, property.getCost())
        else:
            print("TODO")
            #payRent
    def landedJail(self):
        self.properties = 10
        #need to write some code that prevents the player from leaving jail for 3 turns or until they roll doubles

    def landedJustVisiting(self):
        #this function should probably not exist after we check the space we can just have the program do nothing
        print("landedJustVisiting() should probs be deleted")
    def landedFreeParking(self):
        #this function should probably not exist after we check the space we can just have the program do nothing
        print("landedFreeParking() should probs be deleted")

    def landedGo(self):
        #the player is paid there $200 dollars on the dice roll so this function does not need to exist either
        print("landedGo() should probs be deleted")

    def playerLandedComChest(self, comChestCard):
        #no idea how to write this yet
        print("TODO")
    def playerLandedChance(self, chanceCard):
        #no idea how to write this yet
        print("TODO")

    def playerLandedTaxes(self, property):
        self.money -= property.getCost()


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
# 9 = taxes