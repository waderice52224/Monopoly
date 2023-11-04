import random
from Board import *
from player import Player

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


while not isPlayersBankrupt():
    for i in players:
        i.rollDice()
        if board[i.getPosistion()-1].canbuy():
            i.buyProperty(board[i.getPosistion()-1], board[i.getPosistion()-1].getCost())

print(players[0].getMoney())
print(players[1].getMoney())
