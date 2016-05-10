import minimax
from minimax import *
EASY = 1
MEDIUM = 3
HARD = 5
import copy

class humanPlayer:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getColor(self):
        return self.color
    def getName(self):
        return self.name

    def play(self, board):
        dropColNum = input("{} move : ".format(self.name))
        board.Update(dropColNum, self.color)
        return board

class AIPlayer:
    def __init__(self, name, color,level = MEDIUM):
        self.name = name
        self.color = color
        self.level = level

    def getColor(self):
        return self.color
    def getName(self):
        return self.name

    def play(self, board):
        print("{} move : ".format(self.name))
        tempBoard = copy.deepcopy(board)
        node = Node(self.level, 1, board, self.color)
        dropColNum = minimax(node, self.level, 1)
        tempBoard.Update(dropColNum%board.getHeight(), self.color)
        #for child in node.children:
            
        #    if child.getValue() == dropColNum:
        #        board = child.getBoard()
        #        break
        return tempBoard

    