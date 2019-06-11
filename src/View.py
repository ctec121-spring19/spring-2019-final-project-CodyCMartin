# View.py
# 
# For TicTacToe

from graphics import *

class View:

    def __init__(self):
        # Window creation
        self._win = GraphWin("Tic Tac Toe", 600,600)

        # Grid line creation
        Line(Point(200,50),Point(200,550)).draw(self._win)
        Line(Point(400,50),Point(400,550)).draw(self._win)
        Line(Point(50,200),Point(550,200)).draw(self._win)
        Line(Point(50,400),Point(550,400)).draw(self._win)

        # Top text "tic tac toe"
        topText = Text(Point(300,25),"Tic Tac Toe")
        topText.setStyle("bold")
        topText.setSize(18)
        topText.draw(self._win)
        
    # function to return coords when clicked
    def getClick(self):
        point = self._win.getMouse()        
        return(point.getX(), point.getY())

    # this text shows before the start of each game 
    def startText(self):
        starter = Text(Point(300,575),"Click to start a game.")
        starter.setSize(18)
        starter.setStyle("bold")
        starter.draw(self._win)



              
# View test
def viewTest():
    v = View()
    v.startText()
    v.getClick()



viewTest()

   
   
#if __name__ == "__main__":
#    ViewTest()

