# Model.py
#
# For TicTacToe

from View import View


class Model:
    
    def __init__(self, view):
        # had to add a 10th spot on the board for win criteria to read properly 
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        # turn counter for draw criteria 
        self.turns = 8
        self.view = View
        
        
        

    # takes coords and checks if cell if already selected. If not, takes player symbol and popoluates the cells list
    # if a cell is taken, tells view to print out error message to user.
    def cellDef(self,coords, player):


        if coords == (0, 0) and self.cells[0] == " ":
            self.cells[0] = player
            print("cell1")
            print(self.cells)
        elif coords == (1, 0) and self.cells[1] == " ":
            self.cells[1] = player
            print("cell2")
            print(self.cells)
        elif coords == (2, 0) and self.cells[2] == " ":
            self.cells[2] = player
            print("cell3")
            print(self.cells)
        elif coords == (0, 1) and self.cells[3] == " ":
            self.cells[3] = player
            print("cell4")
            print(self.cells)
        elif coords == (1, 1) and self.cells[4] == " ":
            self.cells[4] = player
            print("cell5")
            print(self.cells)
        elif coords == (2, 1) and self.cells[5] == " ":
            self.cells[5] = player
            print("cell6")
            print(self.cells)
        elif coords == (0, 2) and self.cells[6] == " ":
            self.cells[6] = player
            print("cell7")
            print(self.cells)
        elif coords == (1, 2) and self.cells[7] == " ":
            self.cells[7] = player
            print("cell8")
            print(self.cells)
        elif coords == (2, 2) and self.cells[8] == " ":
            self.cells[8] = player
            print("cell9")
            print(self.cells)
        else:
            print("cell full")
        self.turns = self.turns + 1
        self.winCriteria()
       
        

    
    # checking all possible win outcomes and calling on turn counter to call a draw if turns reach 9
    def winCriteria(self):

        if self.cells[0] == "x" and self.cells[1] == "x" and self.cells[2] == "x":
            print("X wins!")       
        elif self.cells[3] == "x" and self.cells[4] == "x" and self.cells[5] == "x":
            print("X wins!") 
        elif self.cells[6] == "x" and self.cells[7] == "x" and self.cells[8] == "x":
            print("X wins!") 
        elif self.cells[0] == "x" and self.cells[3] == "x" and self.cells[6] == "x":
            print("X wins!") 
        elif self.cells[1] == "x" and self.cells[4] == "x" and self.cells[7] == "x":
            print("X wins!") 
        elif self.cells[2] == "x" and self.cells[5] == "x" and self.cells[8] == "x":
            print("X wins!") 
        elif self.cells[0] == "x" and self.cells[4] == "x" and self.cells[8] == "x":
            print("X wins!") 
        elif self.cells[2] == "x" and self.cells[4] == "x" and self.cells[6] == "x":
            print("X wins!") 
        elif self.cells[0] == "o" and self.cells[1] == "o" and self.cells[2] == "o":
            print("O wins!")
        elif self.cells[3] == "o" and self.cells[4] == "o" and self.cells[5] == "o":
            print("O wins!")
        elif self.cells[6] == "o" and self.cells[7] == "o" and self.cells[8] == "o":
            print("O wins!")
        elif self.cells[0] == "o" and self.cells[3] == "o" and self.cells[6] == "o":
            print("O wins!")
        elif self.cells[1] == "o" and self.cells[4] == "o" and self.cells[7] == "o":
            print("O wins!")
        elif self.cells[2] == "o" and self.cells[5] == "o" and self.cells[8] == "o":
            print("O wins!")
        elif self.cells[0] == "o" and self.cells[4] == "o" and self.cells[8] == "o":
            print("O wins!")
        elif self.cells[2] == "o" and self.cells[4] == "o" and self.cells[6] == "o":
            print("O wins!")
        elif self.turns == 9:
            print("draw")
            
        print("Number of turns taken", self.turns)

    
        
        

    
        





def ModelTest():
    model = Model()
    model.cellDef(20,"X")
    

    

if __name__ == "__main__":
    ModelTest()
