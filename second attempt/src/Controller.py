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
        selectionX = m.cellSelectionX(v.getClick() # think this is breaking it only one selection 
        player1Turn = True
        player2Turn = True
        game = True
       

        # main game loop. game value to be changed upon win or draw to exit
        while game == True:

            # player turn loops

            if selectionX == False:
                v.startText("Cell populated. You lose a turn")
            elif player1Turn == True:
                v.startText("Player X's turn")
                m.cellSelectionX(click)
                print(click)
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
