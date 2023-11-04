import properties
from Spaces import Space

class Chance:
    def __init__(self, val, money, goto, jail):
        self.val = val
        self.money = money
        self.goto = goto
        self.jail = jail


c1 = Chance(0, properties.p24, False)
c2 = Chance(2, "Advance to nearest Railroads, pay double", False)
c3 = Chance(0, properties.p39, False)
c4 = Chance(0, False, True)
c5 = Chance(50, False, False)
c6 = Chance(50, False, False)
c7 = Chance(0, "Advance to Reading Railroad", False)
c8 = Chance(0, properties.p11, False)
c9 = Chance(2, "Advance to nearest Railroads, pay double", False)
c10 = Chance(-15, False, False)
c11 = Chance(0, -3, False)
c12 = Chance(150, False, False)
c13 = Chance(0, "Make General Repairs: Pay 25, Pay 100", False)
c14 = Chance(0, "Pay each player 50", False)
c15 = Chance(0, 0, False)
c16 = Chance(0, "Nearest utility, Pay 10x instead of 4x", False)
