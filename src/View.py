# View.py
# 
# For TicTacToe

from graphics import *


# View class creation
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
        self.topText = Text(Point(300,25),"Tic Tac Toe")
        self.topText.setStyle("bold")
        self.topText.setSize(18)
        self.topText.draw(self._win)

        # Bottom text formatting and location 
        self.bottomText = Text(Point(300,575),"")
        self.bottomText.setStyle("bold")
        self.bottomText.setSize(18)
        self.bottomText.draw(self._win)
        
        
    # function to return coords when clicked
    def getClick(self):
        point = self._win.getMouse()        
        return(point.getX(), point.getY())

    # this text shows before the start of each game 
    def startText(self, message):
        self.bottomText.setText(message)
        
                  
# View test
def ViewTest():
    v = View()
    v.startText("test")
    v.getClick()
    print(v.getClick())
   
    
   
if __name__ == "__main__":
    ViewTest()

