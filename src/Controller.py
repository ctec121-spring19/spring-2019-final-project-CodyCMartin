# Controller.py
#
# For TicTacToe

from View import *
from Model import *

class Controller:

    def __init__(self):
       
        v = View()
        m = Model()
        click = v.getClick
        selectionX = m.cellSelectionX(v.getClick())
       

        
        v.startText("Player X's turn")
        m.cellSelectionX(click)
        print(selectionX)
        if selectionX == False:
            v.startText("Cell populated. You lose a turn")
        v.drawSymbol("PlayerX")

        


          
            
        
      
      
        



        input()

    
        
    
        

      

    
def ControllerTest():
    c  = Controller()
    input()
        

if __name__ == "__main__":
    ControllerTest()
