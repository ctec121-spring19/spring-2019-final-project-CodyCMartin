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
        self.bottomText = Text(Point(1.5,.12),"")
        self.bottomText.setStyle("bold")
        self.bottomText.setSize(18)
        self.bottomText.draw(self._win)
        
        
    # function to return coords when clicked
    def getClick(self):
        point = self._win.getMouse()        
        return int(point.getX()), int(point.getY())

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

