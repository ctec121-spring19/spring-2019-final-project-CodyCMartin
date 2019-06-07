# Final.py


# Cody Martin
# Input - User clicks based on turn
# Process - The model draws either an X or O depending on turn and if game is ongoing. 
# Output - Draws X or O based on if the game is ongoing. If not, user is asked to play again or quit




from graphics import *


def view():

    # Initial screen build

    win = GraphWin("Tic Tac Toe", 600,600)
    vertical_line1 = Line(Point(200,50),Point(200,550))
    vertical_line2 = Line(Point(400,50),Point(400,550))
    horizontal_line1 = Line(Point(50,200),Point(550,200))
    horizontal_line2 = Line(Point(50,400),Point(550,400))
    headertext = Text(Point(300,25),"Tic Tac Toe")
    headertext.setStyle("bold")
    headertext.setSize(18)

    # All draws for intial screen build 

    vertical_line1.draw(win)
    vertical_line2.draw(win)
    horizontal_line1.draw(win)
    horizontal_line2.draw(win)
    headertext.draw(win)
    

    myImage = Image(Point(5,5), "C:\Users\Codyc\OneDrive\Desktop\Lettre_X_cuisinier_herisson_CFZ")
    myImage.draw(win)


    input()




view()



