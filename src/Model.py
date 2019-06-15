# Model.py
#
# For TicTacToe





boarD = ["","","",
        "","",""
        "","","", "", ""]


class Model:

    def __init__(self):
        self._model = Model
       
       

    # populated board list to track player moves. Validates if cell is already populated through if loop
    def cellSelectionX(self,cell):
        # local variable to board 
        board = boarD
        
        
        # populating the list board with player moves. Return cell location to controller to draw with view
        if cell == "cell1" and board[0] == "":
            board[0] = "X"
            return cell
        elif cell == "cell1" and board[0] != "":
            return False
        elif cell == "cell2" and board[1] == "":
            board[1] = "X"
            return cell
        elif cell == "cell2" and board[1] != "":
            return False
        elif cell == "cell3" and board[2] == "":
            board[2] = "X"
            return cell
        elif cell == "cell3" and board[2] != "":
            return False
        elif cell == "cell4" and board[3] == "":
            board[3] = "X"
            return cell
        elif cell == "cell4" and board[3] != "":
            return False
        elif cell == "cell5" and board[4] == "":
            board[4] = "X"
            return cell
        elif cell == "cell5" and board[4] != "":
            return False
        elif cell == "cell6" and board[5] == "":
            board[5] = "X"
            return cell
        elif cell == "cell6" and board[5] != "":
            return False
        elif cell == "cell7" and board[6] == "":
            board[6] = "X"
            return cell
        elif cell == "cell7" and board[6] != "":
            return False
        elif cell == "cell8" and board[7] == "":
            board[7] = "X"
            return cell
        elif cell == "cell8" and board[7] != "":
            return False
        elif cell == "cell9" and board[8] == "":
            board[8] = "X"
            return cell
        elif cell == "cell9" and board[8] != "":
            return False
        elif cell == "cell9" and board[9] == "":
            board[9] = "X"
            return cell
        elif cell == "cell9" and board[9] != "":
            return False
        






    
    

# test
#def ModelTest():
    #m = Model()
    #m.cellSelectionX("cell1")
    #m.cellSelectionO("cell2")
    #print(boarD)
    
    
    
    
    


#if __name__ == "__main__":
    #ModelTest()
    
