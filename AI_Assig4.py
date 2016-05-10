from player import *#Player, humanPlayer, AIPlayer
import copy
from minimax import *
#
#       The core game class
#
class Game:

        def __init__(self, player1, player2, playboard, Level):
                self.PLAYER1 = player1;  self.PLAYER2 = player2
                self.PLAYBOARD = playboard; self.LEVEL = Level;

        def Start(self):
                # Game loop
                while True:
                    Renderer.render(self.PLAYBOARD.getPad())
                    self.PLAYBOARD = self.PLAYER1.play(self.PLAYBOARD)

                    if self.Terminal_State(self.PLAYER1.getColor()):
                        Renderer.render(self.PLAYBOARD.getPad())
                        print("{} is the winner!!!!!".format(str(self.PLAYER1.getName())))
                        break

                    Renderer.render(self.PLAYBOARD.getPad())
                    self.PLAYBOARD = self.PLAYER2.play(self.PLAYBOARD)
                    if self.Terminal_State(self.PLAYER2.getColor()):
                        Renderer.render(self.PLAYBOARD.getPad())
                        print("{} is the winner!!!!!".format(str(self.PLAYER2.getName())))
                        break

                
        def Terminal_State(self, color):
            [fourCounter, threeCounter, twoCounter, fourCounterCol, threeCounterCol,twoCounterCol] = self.PLAYBOARD.getBlocksInRow(color)
            if fourCounter or fourCounterCol:
                return True
            if len(self.PLAYBOARD.getAvailable()) == 0:
                return True
            return False



#
#       THE GAME BOARD
#

class Board:

        def __init__(self, Height, width, initColor):
                self.Height = Height
                self.Width = width
                self.initColor = initColor
                self.pad = [[initColor for i in range(0, self.Width)] for j in range(0, self.Height)]
                self.pad[len(self.pad)-1] = ['A' for i in range(0,self.Width)]

        def Update(self, column, color):
                flag = False
                for i in range(0, self.Height):                         # Setting the user input
                        if self.pad[i][column] == 'A':
                                self.pad[i][column] = color
                                flag = True
                        if ((flag) and (i <= self.Height) and not i<=0):
                                self.pad[i-1][column] = 'A'
                                break
                return flag
        def update(self, column, color, nonA):
                flag = False
                for i in range(0, self.Height):                         # Setting the user input
                        if self.pad[i][column] == 'A':
                                self.pad[i][column] = color
                                flag = True
                        if nonA:
                                self.pad[i-1][column] = 'A'
                                break
                return flag

        def getAvailable(self):
                return [j for i in range(0, self.Height) for j in range(0, self.Width) if self.pad[i][j] == 'A']

        def getPad(self):
                return self.pad

        def getHeight(self):
                return self.Height

        def getWidth(self):
                return self.Width
        def getBlocksInRow(self, color):
                copySelf = copy.deepcopy(self)
                transposedPad = zip(*copySelf.pad)
                transposedPad = [list(i) for i in transposedPad]

                fourCounter = 0
                threeCounter = 0
                twoCounter = 0

                fourCounterCol = 0
                threeCounterCol = 0
                twoCounterCol = 0
                
                fourInRow = [color, color, color, color]
                threeInRow = [color, color, color]
                twoInRow = [color, color]

                for i in range(0, self.Height):
                        tempRow = copySelf.pad[i]
                        fourRowIndex = [(j, j+len(fourInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(fourInRow)] == fourInRow]
                        if len(fourRowIndex) > 0:
                                fourCounter = fourCounter + len(fourRowIndex)
                                for tempIndex in fourRowIndex:
                                        copySelf.pad[i][tempIndex[0]:tempIndex[1]] = ['4','4','4','4']

                for i in range(0, self.Height):
                        tempRow = copySelf.pad[i]
                        threeRowIndex = [(j, j+len(threeInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(threeInRow)] == threeInRow]
                        if len(threeRowIndex) > 0:
                                threeCounter = threeCounter + len(threeRowIndex)
                                for tempIndex in fourRowIndex:
                                        copySelf.pad[i][tempIndex[0]:tempIndex[1]] = ['3','3','3']


                for i in range(0, self.Height):
                        tempRow = copySelf.pad[i]
                        twoRowIndex = [(j, j+len(twoInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(twoInRow)] == twoInRow]
                        if len(twoRowIndex) > 0:
                                twoCounter = twoCounter + len(twoRowIndex)
                                for tempIndex in twoRowIndex:
                                        copySelf.pad[i][tempIndex[0]:tempIndex[1]] = ['2','2']

                ###########################################################################################

                for i in range(0, self.Width): #equivelat to the transpose height
                        tempRow = transposedPad[i]
                        fourRowIndex = [(j, j+len(fourInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(fourInRow)] == fourInRow]
                        if len(fourRowIndex) > 0:
                                fourCounterCol = fourCounterCol + len(fourRowIndex)
                                for tempIndex in fourRowIndex:
                                        transposedPad[i][tempIndex[0]:tempIndex[1]] = ['4','4','4','4']

                for i in range(0, self.Width):
                        tempRow = transposedPad[i]
                        threeRowIndex = [(j, j+len(threeInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(threeInRow)] == threeInRow]
                        if len(threeRowIndex) > 0:
                                threeCounterCol = threeCounterCol + len(threeRowIndex)
                                for tempIndex in fourRowIndex:
                                        transposedPad[i][tempIndex[0]:tempIndex[1]] = ['3','3','3']


                for i in range(0, self.Width):
                        tempRow = transposedPad[i]
                        twoRowIndex = [(j, j+len(twoInRow)) for j in range(len(tempRow)) if tempRow[j:j+len(twoInRow)] == twoInRow]
                        if len(twoRowIndex) > 0:
                                twoCounterCol = twoCounterCol + len(twoRowIndex)
                                for tempIndex in twoRowIndex:
                                        transposedPad[i][tempIndex[0]:tempIndex[1]] = ['2','2']
                                        

                

                ret = [fourCounter, threeCounter, twoCounter, fourCounterCol,threeCounterCol,twoCounterCol]
                return ret

#       The Renderer Class Mainly for display
#

class Renderer:
        def __init__(self):
                pass
        @staticmethod
        def initial():
                print("\t\tWelcome to 4 connect")
                print("Connect 4 is two-player connection game in which the players first choose a color and then\n"+
                          "take turns dropping colored discs from the top into a suspended grid.")

        @staticmethod
        def render(pad):
                for i in range(0,len(pad)):
                        print(pad[i])
        
        #@staticmethod
        #def render(player):
        #       pass

if __name__ == '__main__':
        myboard = Board(6, 7, '*');
        x = input("Enter 1--> user vs user, 2 --> user vs AI, 3 --> AI vs AI : ")
        x = int(x)
        if x == 1:
            name1 = raw_input("Player 1 name: ")
            name2 = raw_input("Player 2 name: ")
            player1 = humanPlayer(name1, 'x')
            player2 = humanPlayer(name2,'o')
        elif x == 2:
            name1 = raw_input("Player 1 name: ")
            lev = input("Enter the level of difficulty (1:easy, 3:medium, 5:hard): ")
            lev = int(lev)
            player1 = humanPlayer(name1, 'x')
            player2 = AIPlayer("AI",'o', lev)
        elif x == 3:
            lev = input("Enter the level of difficulty: ")
            lev = int(lev)
            player1 = AIPlayer("AI 1 ", 'x', lev)
            player2 = AIPlayer("AI 2 ",'o', 10)
        else:
            print("Wrong choice")
            exit()
        
        myGame = Game(player1, player2, myboard, 1)
        myGame.Start()
