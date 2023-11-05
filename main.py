import random

from player import Player
from monopoly.Board import *
players = []
def makePlayer(playerName):
    player = Player(playerName, 40, 1500, [])
    return player


def isPlayersBankrupt():
    for i in players:
        if i.getMoney() <= 0:
            return True
    return False


# playerCount = int(input("How Many Players: "))
playerCount = 2

if playerCount > 4 or playerCount < 2:
    print("Player count needs to be 4 or less, and greater than 1: ")
    playerCount = int(input("How Many Players"))


for i in range(playerCount):
    players.append(makePlayer("Player " + str(i + 1)))

test = random.randint(0, 39)
players[0].checkSpace(board[test])
print(board[test].getNameOfSpace())
print((board[test].getCost()))

print()
print(players[0].getName())
print(players[0].getMoney())
if len(players[0].properties) > 0:
    print(players[0].properties[0].getNameOfSpace())
else:
    print("Player has no properties")





#A very Basic game loop that lets players buy properties
# while not isPlayersBankrupt():
#     for i in players:
#         i.rollDice()
#         if board[i.getPosistion()-1].canbuy():
#             i.buyProperty(board[i.getPosistion()-1], board[i.getPosistion()-1].getCost())


