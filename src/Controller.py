# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

class Controller:

    def __init__(self):
        self._v = View()
        self._v.startText("Click to start a game!")
        self._v.getClick()
        self._v.startText("Player X's turn!")
        self._v.getClick()

        

        # Call view to draw window and grid
        # Call view to draw start game text
        # Call view to get click for start of game
        # Call view to draw player 1 turn text
        # Get mouse input from user 
        # Verify coords from mouse input is in cell
        # Translate cell location is valid cell location
        # Call model to see if cell is empty or full
        # if full call view to draw "cell full" text
        # if empty, tell draw to draw player symbol into cell
        

        

        


def ControllerTest():
    c = Controller()
    input()
    
    

if __name__ == "__main__":
    ControllerTest()
