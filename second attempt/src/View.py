# View.py
# 
# For TicTacToe

from graphics import *


# View class creation
class View:

    def __init__(self):
        # Window creation/coords
        self._win = GraphWin("Tic Tac Toe", 600,600)
        self._win.setCoords(0, 0, 3, 3)

        # Grid line creation
        Line(Point(1,.25),Point(1,2.75)).draw(self._win)
        Line(Point(2,.25),Point(2,2.75)).draw(self._win)
        Line(Point(.25,1),Point(2.75,1)).draw(self._win)
        Line(Point(.25,2),Point(2.75,2)).draw(self._win)

        # Top text "tic tac toe"
        self.topText = Text(Point(1.5,2.92),"Tic Tac Toe")
        self.topText.setStyle("bold")
        self.topText.setSize(18)
        self.topText.draw(self._win)

        # Bottom text formatting and location 
        self.bottomText = Text(Point(1.5,.12),"Player X's turn")
        self.bottomText.setStyle("bold")
        self.bottomText.setSize(18)
        self.bottomText.draw(self._win)

        # Symbol text
        self.symbol = Text(Point(1.5,1.5), "")
        self.symbol.setStyle("bold")
        self.symbol.setSize(24)
        self.symbol.draw(self._win)        
        
    # function to return coords as ints when clicked then send cell location to model
    def getClick(self):
        point = self._win.getMouse()        
        pX = int(point.getX())
        pY = int(point.getY())

        if pX == 0 and pY == 0:
            return "cell1"
        elif pX == 1 and pY == 0:
            return "cell2"
        elif pX == 2 and pY == 0:
            return "cell3"
        elif pX == 0 and pY == 1:
            return "cell4"
        elif pX == 1 and pY == 1:
            return "cell5"
        elif pX == 2 and pY == 1:
            return "cell6"
        elif pX == 0 and pY == 2:
            return "cell7"
        elif pX == 1 and pY == 2:
            return "cell8"
        elif pX == 2 and pY == 2:
            return "cell9"

    # this text is located at the bottom of the window and informs players of whos turn it is 
    def startText(self, message):
        self.bottomText.setText(message)

    def drawSymbol(self, symbol):
        if symbol == "PlayerX":
            self.symbol.setText("X")
        elif symbol == "PlayerO":
            self.symbol.setText("O")

    
    

                  
# View test
#def ViewTest():
    #v = View()
    #v.startText("test")
    #v.getClick()
    #print(v.getClick())
    #v.drawSymbol("PlayerX")
   # input()
   
    
   
#if __name__ == "__main__":
  #  ViewTest()

