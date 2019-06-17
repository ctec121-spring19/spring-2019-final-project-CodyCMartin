# Controller.py
#
# For TicTacToe

from View import View
from Model import Model


        


def main():
    view = View()
    model = Model(view)
    playerX = "x"
    playerO = "o"
    
    

    
    # calls for click coords from view for player X turn 
    click = view.setClick()
    # supplies coords to model for placement
    model.cellDef(click, playerX)
    

    # calls for click coords from view for player X turn  
    click = view.setClick()
    # supplies coords to model for placement
    model.cellDef(click, playerO)
    
    





    

main()

    



def ControllerTest():
    # delete and enter your code here
    pass

if __name__ == "__main__":
    ControllerTest()
