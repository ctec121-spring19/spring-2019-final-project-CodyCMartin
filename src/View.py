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

    # text at bottom of screen to notify player x thats its their turn
    def playerX_Turn(self):
        playerX = Text(Point(300,575),"Player X's turn! ")
        playerX.setSize(18)
        playerX.setStyle("bold")
        playerX.draw(self._win)

    # text at bottom of screen to notify player x thats its their turn
    def playerO_Turn(self):
        playerO = Text(Point(300,575),"Player O's turn! ")
        playerO.setSize(18)
        playerO.setStyle("bold")
        playerO.draw(self._win)

    # Error message to pop up when a player picks a cell thats already populated
    def cellTaken(self):
        cellTaken = Text(Point(300,575),"Cell already taken!")
        cellTaken.setSize(18)
        cellTaken.setStyle("bold")
        cellTaken.draw(self._win)
        





              
# View test
def viewTest():
    v = View()
    v.startText()
    v.getClick()
    v.playerO_Turn()
    v.playerX_Turn()
    v.cellTaken()
    




viewTest()

   
   
#if __name__ == "__main__":
#    ViewTest()

