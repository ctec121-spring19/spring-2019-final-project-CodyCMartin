# Model.py
#
# For TicTacToe

from View import View


class Model:

    def __init__(self):
        self._v = View()
        
        

    # populated board list to track player moves. Validates if cell is already populated through if loop
    def cellSelection(self, cell):
        
        board = ["","","",
            "","",""
            "","","", ""]
    

        if cell == "cell1" and board[0] == "":
            return True
        elif cell == "cell1" and board[0] != "":
            return False
        if cell == "cell2" and board[2] == "":
            return True
        elif cell == "cell2" and board[2] != "":
            return False
        if cell == "cell3" and board[3] == "":
            return True
        elif cell == "cell3" and board[3] != "":
            return False
        if cell == "cell4" and board[4] == "":
            return True
        elif cell == "cell4" and board[4] != "":
            return False
        if cell == "cell5" and board[5] == "":
            return True
        elif cell == "cell5" and board[5] != "":
            return False
        if cell == "cell6" and board[6] == "":
            return True
        elif cell == "cell6" and board[6] != "":
            return False
        if cell == "cell7" and board[7] == "":
            return True
        elif cell == "cell7" and board[7] != "":
            return False
        if cell == "cell8" and board[8] == "":
            return True
        elif cell == "cell8" and board[8] != "":
            return False
        if cell == "cell9" and board[9] == "":
            return True
        elif cell == "cell9" and board[9] != "":
            return False
    

def ModelTest():
    m = Model()
    m.cellSelection("cell1")
    
    
    
    
    
    pass

if __name__ == "__main__":
    ModelTest()
