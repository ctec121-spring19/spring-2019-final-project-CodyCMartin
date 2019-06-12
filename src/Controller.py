# Controller.py
#
# For TicTacToe

from View import View
from Model import Model

class Controller:

    def __init__(self):
        self._model = Model()
        self._view = View()
        self._view.startText("Click to start a game!")
        self._view.getClick()
        self._view.startText("Player X's turn!")
        


    def cellReport(self):

        # Defining the click recieved from view
        cells = self._view.getClick()

        # Sending the click to be varified and housed to model
        self._model.cellSelection(cells)

        # Defining the return value of the varification from model 
        cellSelect = self._model.cellSelection()

        # proving the connections are working properly 
        if cellSelect == True:
            print("working")
        

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
    c.cellReport("cell1")
        

if __name__ == "__main__":
    ControllerTest()
