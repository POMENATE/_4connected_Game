from sys import maxsize
from AI_Assig4 import *

class Node(object):
    def __init__(self, depth, playerNum, board, color, value=0):
        self.depth = depth
        self.playerNum = playerNum
        self.board = board
        self.value = value
        self.color = color
        self.run = self.board.getAvailable()
        #self.color.append(color)
        self.children = []
        self.createChildren(['','o','x'])

    def createChildren(self, color):
        if self.depth < 0 :
            return
        for i in self.run:
            tempBoard = self.board
            if tempBoard.update(i, self.color, False):
                b = tempBoard
            else:
                return
            self.children.append(Node(self.depth - 1, -self.playerNum, b, color[-self.playerNum],self.utility()))

    def utility(self):
        if self.color == 'o':
            color2 = 'x'
        else :
            color2 = 'o'
        [fourCounter, threeCounter, twoCounter, fourCounterCol, threeCounterCol,twoCounterCol] = self.board.getBlocksInRow(self.color)
        [fourCounter2, threeCounter2, twoCounter2, fourCounterCol2, threeCounterCol2, twoCounterCol2] = self.board.getBlocksInRow(color2)

        utilityValue = ((fourCounter+fourCounterCol)*100000) + ((threeCounter+threeCounterCol)*100)+(twoCounter+twoCounterCol)
        utilityValue2 = ((fourCounter2+fourCounterCol2)*100000) + ((threeCounter2+threeCounterCol2)*100)+(twoCounter2+twoCounterCol2)
        return (utilityValue - utilityValue2)

    def getValue(self):
        return self.value
    def getBoard(self):
        return self.board

def minimax(node, depth, playerNum):
    if (depth == 0) :#or (abs(node.getValue()) == maxsize):
        return node.getValue()

    bestValue = maxsize * -playerNum
    for child in node.children:
        val = minimax(child, depth -1, -playerNum)
        if abs(maxsize * playerNum - val) < abs(maxsize * playerNum - bestValue):
            bestValue = val
    return bestValue