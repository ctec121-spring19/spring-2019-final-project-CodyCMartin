# View.py
# 
# For TicTacToe

from graphics import *

    

class View:
    def __init__(self):
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

        self.bottomText = Text(Point(1.5,.18),"test")
        self.bottomText.setStyle("bold")
        self.bottomText.setSize(18)
        self.bottomText.draw(self._win)

        

    def setClick(self):
        point = self._win.getMouse()        
        pX = int(point.getX())
        pY = int(point.getY())
        print(pX,pY)
        return(pX, pY)

    def bottomMessage(self, msg):
        self.bottomText.setText()
        
        

        
    

    
    


        

def ViewTest():
    v = View()
    v.bottomMessage("Test")
    v.setClick()
    
   
    
    
if __name__ == "__main__":
    ViewTest()
