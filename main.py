import random
from properties import Properties
from Spaces import Space

# playerCount = eval(input("How many players :"))
# playerMortgage = eval(input("Would you like your player to mortgage, (1 or yes, 2 for no): "))
# playerMortgageMonopolies = ""
# if playerMortgage == 1:
#     playerMortgage = True
#     playerMortgageMonopolies = eval(input("Can mortgage monopolies to buy another property? (1 = yes, 2 = no): "))
# else:
#     playerMortgage: False
# if playerMortgageMonopolies == 1:
#     playerMortgageMonopolies = True
# else:
#     playerMortgageMonopolies = False
p1 = Properties("Mediterranean Avenue", 1, 2, 4, 10, 30, 90, 160, 250, 50, 60, 30, 33)
p2 = Space(2) #comChest
p3 = Properties("Baltic Avenue", 3, 4, 8, 20, 60, 180, 320, 450, 50, 60, 30, 33)
p4 = Space(4) #incometax
p5 = Space(5) #Properties("Reading Railroad", rent1=25, rent2=50, rent3=100, rent4=200, mortgage=100, unmortgage=110)
p6 = Properties("Oriental Avenue", 6, 6, 12, 30, 90, 270, 400, 550, 50, 100, 50, 55)
p7 = Space(7) #Chance
p8 = Properties("Vermont Avenue", 8, 6, 12, 30, 90, 270, 400, 550, 50, 100, 50, 55)
p9 = Properties("Connecticut Avenue",9,  8, 16, 40, 100, 300, 450, 600, 50, 120, 60, 66)
p10 = Space(10) # just viz
p11 = Properties("St.Charles Place", 11, 10, 20, 50, 150, 450, 625, 750, 100, 140, 70, 77)
p12 = Space(12)#Properties("Electric Company")
p13 = Properties("States Avenue", 13, 10, 20, 50, 150, 450, 625, 750, 100, 140, 70, 77)
p14 = Properties("Virgina Avenue", 14, 12, 24, 60, 180, 500, 700, 900, 100, 160, 80, 88)
p15 = Space(15)#Properties("Pennsylvania Railroad", rent1=25, rent2=50, rent3=100, rent4=200, mortgage=100, unmortgage=110)
p16 = Properties("St.James Place", 16, 14, 28, 70, 200, 550, 750, 950, 100, 180, 90, 99)
p17 = Space(17) #comChest
p18 = Properties("Tennessee Avenue", 18, 14, 28, 70, 200, 550, 750, 950, 100, 180, 90, 99)
p19 = Properties("New York Avenue", 19, 16, 32, 80, 220, 600, 800, 1000, 100, 200, 100, 110)
p20 = Space(20) # Free Parking
p21 = Properties("Kentucky Avenue", 21, 18, 36, 90, 250, 700, 875, 1050, 150, 220, 110, 121)
p22 = Space(22) #chance
p23 = Properties("Indiana Avenue", 23, 18, 36, 90, 250, 700, 875, 1050, 150, 220, 110, 121)
p24 = Properties("Illinois Avenue", 24, 20, 40, 100, 300, 750, 925, 1100, 150, 240, 220, 132)
p25 = Space(25) #Properties("B & O Railroad", rent1=25, rent2=50, rent3=100, rent4=200, mortgage=100, unmortgage=110)
p26 = Properties("Atlantic Avenue", 26, 22, 44, 110, 330, 800, 975, 1150, 150, 260, 130, 143)
p27 = Properties("Ventnor Avenue", 27, 22, 44, 110, 330, 800, 975, 1150, 150, 260, 130, 143)
p28 = Space(28) #Properties("Water Works")
p29 = Properties("Marvin Gardens", 29, 24, 48, 120, 360, 850, 1025, 1200, 150, 280, 140, 154)
p30 = Space(30) #go to jail
p31 = Properties("Pacific Avenue", 31, 26, 52, 130, 390, 900, 1100, 1275, 200, 300, 150, 165)
p32 = Properties("North Carolina Avenue", 32, 26, 52, 130, 390, 900, 1100, 1275, 200, 300, 150, 165)
p33 = Space(33) #comChest
p34 = Properties("Pennsylvania Avenue", 34, 28, 56, 150, 450, 1000, 1200, 1400, 200, 320, 160, 176)
p35 = Space(35) #Properties("Short Line", rent1=25, rent2=50, rent3=100, rent4=200, mortgage=100, unmortgage=110)
p36 = Space(36) # chance
p37 = Properties("Park Place", 37, 35, 70, 175, 500, 1100, 1300, 1500, 200, 350, 175, 193)
p38 = Space(38) # luxury tax
p39 = Properties("Boardwalk", 39, 50, 100, 200, 600, 1400, 1700, 2000, 200, 400, 200, 220)
p40 = Space(40) # Go

board = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40]



for i in board:
    print(i.getNameOfSpace(), end=' ')
    print(i.spaceVal)
def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

playersBankrupt = False
# while not playersBankrupt:
    # all the code



