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
        player1Turn = True
        player2Turn = True
        game = True
       
        while game == True:
            if player1Turn == True:
                v.startText("Player X's turn")
                m.cellSelectionX(click)
                print(click)
            elif selectionX == False:
                v.startText("Cell populated. You lose a turn")
            v.drawSymbol("PlayerX")
            player2Turn == True
            player1Turn == False


            if player2Turn == True:
                v.startText("Player O's turn")
                m.cellSelectionX(click)
                print(selectionX)
                if selectionX == False:
                    v.startText("Cell populated. You lose a turn")
                v.drawSymbol("PlayerX")
                player2Turn == False
                player1Turn == True
                game = False
        


          
            
        
      
      

      

    
def ControllerTest():
    c  = Controller()
    input()
        

if __name__ == "__main__":
    ControllerTest()
