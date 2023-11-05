from Properties import Property
from Spaces import Space
from Utilities import Utility
from RailRoads import RailRoad



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
#def __init__(self, name, val, rent, typeSpace, cost, mortgage, unmortgage):

p1 = Property("Mediterranean Avenue", 1, 2, 4, 10, 30, 90, 160, 250, 50, 0, 60, 30, 33)
p2 = Space("Community Chest", 2, 7)
p3 = Property("Baltic Avenue", 3, 4, 8, 20, 60, 180, 320, 450, 50, 0, 60, 30, 33)
p4 = Space("Income Tax", 4, 9, 200)
p5 = RailRoad("Reading Railroad", 5, 25, 1, 200, 100, 110)
p6 = Property("Oriental Avenue", 6, 6, 12, 30, 90, 270, 400, 550, 50, 0, 100, 50, 55)
p7 = Space("Chance", 7, 8)
p8 = Property("Vermont Avenue", 8, 6, 12, 30, 90, 270, 400, 550, 50, 0, 100, 50, 55)
p9 = Property("Connecticut Avenue", 9, 8, 16, 40, 100, 300, 450, 600, 50, 0, 120, 60, 66)
p10 = Space("In Jail, Just Visiting", 10, 5)
p11 = Property("St.Charles Place", 11, 10, 20, 50, 150, 450, 625, 750, 100, 0, 140, 70, 77)
p12 = Utility("Electric Company", 12, 2, 150, 75, 82)
p13 = Property("States Avenue", 13, 10, 20, 50, 150, 450, 625, 750, 100, 0, 140, 70, 77)
p14 = Property("Virgina Avenue", 14, 12, 24, 60, 180, 500, 700, 900, 100, 0, 160, 80, 88)
p15 = RailRoad("Pennsylvania Railroad", 15, 25, 1, 200, 100, 110)
p16 = Property("St.James Place", 16, 14, 28, 70, 200, 550, 750, 950, 100, 0, 180, 90, 99)
p17 = Space("Community Chest", 17, 7)
p18 = Property("Tennessee Avenue", 18, 14, 28, 70, 200, 550, 750, 950, 100, 0, 180, 90, 99)
p19 = Property("New York Avenue", 19, 16, 32, 80, 220, 600, 800, 1000, 100, 0, 200, 100, 110)
p20 = Space("Free Parking", 20, 5)
p21 = Property("Kentucky Avenue", 21, 18, 36, 90, 250, 700, 875, 1050, 150, 0, 220, 110, 121)
p22 = Space("Chance", 22, 8)
p23 = Property("Indiana Avenue", 23, 18, 36, 90, 250, 700, 875, 1050, 150, 0, 220, 110, 121)
p24 = Property("Illinois Avenue", 24, 20, 40, 100, 300, 750, 925, 1100, 150, 0, 240, 220, 132)
p25 = RailRoad("B & O Railroad", 25, 25, 1, 200, 100, 110)
p26 = Property("Atlantic Avenue", 26, 22, 44, 110, 330, 800, 975, 1150, 150, 0, 260, 130, 143)
p27 = Property("Ventnor Avenue", 27, 22, 44, 110, 330, 800, 975, 1150, 150, 0, 260, 130, 143)
p28 = Utility("Water Works", 28, 2, 150, 75, 82)
p29 = Property("Marvin Gardens", 29, 24, 48, 120, 360, 850, 1025, 1200, 150, 0, 280, 140, 154)
p30 = Space("Go to jail", 30, 3)
p31 = Property("Pacific Avenue", 31, 26, 52, 130, 390, 900, 1100, 1275, 200, 0, 300, 150, 165)
p32 = Property("North Carolina Avenue", 32, 26, 52, 130, 390, 900, 1100, 1275, 0, 200, 300, 150, 165)
p33 = Space("Community Chest", 33, 7)
p34 = Property("Pennsylvania Avenue", 34, 28, 56, 150, 450, 1000, 1200, 1400, 200, 0, 320, 160, 176)
p35 = RailRoad("Short Line", 35, 25, 1, 200, 100, 110)
p36 = Space("Chance", 36, 8)
p37 = Property("Park Place", 37, 35, 70, 175, 500, 1100, 1300, 1500, 200, 0, 350, 175, 193)
p38 = Space("Luxury Tax", 38, 9, 100)
p39 = Property("Boardwalk", 39, 50, 100, 200, 600, 1400, 1700, 2000, 200, 0, 400, 200, 220)
p40 = Space("Go", 40, 6, -200)

board = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40]