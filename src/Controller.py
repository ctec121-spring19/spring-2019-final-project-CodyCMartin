# Controller.py
#
# For TicTacToe

from View import View
from Model import Model 

class Controller:

    def __init__(self):
       
        v = View()
        m = Model()
        selectionX = m.cellSelectionX(v.getClick())
        selectionO = m.cellSelectionO(v.getClick())
        
        

        v.startText("Player X's turn")
        m.cellSelectionX(v.getClick())
        print(selectionX)
        if selectionX == False:
            v.startText("Pick another cell")
        v.drawSymbol("PlayerX")
        v.startText("Player O's Turn")



        input()

    
        
        



    
        
    
    

        
      
        
       
        

    

   
        

    
def ControllerTest():
    c  = Controller()
    input()
        

if __name__ == "__main__":
    ControllerTest()
