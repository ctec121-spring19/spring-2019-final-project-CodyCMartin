# Final.py


# Cody Martin

# Input - User clicks based on turn
# Process - The model draws either an X or O depending on turn and if game is ongoing. 
# Output - Draws X or O based on if the game is ongoing. If not, user is asked to play again or quit


from graphics import *
import pygame
import time

# list for player positions 

board = ["","","",
         "","",""
         "","","", ""]


# win criteria definitions 

def xwincriteria():
    
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        winx() 
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        winx()
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        winx()
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        winx()
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        winx()
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        winx()
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        winx()
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        winx()
    
    

def owincriteria():
    
    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        wino() 
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        wino()
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        wino()
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        wino()
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        wino()
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        wino()
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        wino()
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        wino()
               
def winx():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("win.wav"), maxtime=6000)
    winnerwin = GraphWin("winner!", 400,400)
    xwintext = Text(Point(200,200),"X wins! Click to start another game.")
    xwintext.draw(winnerwin)
    winnerwin.getMouse()
    winnerwin.close()
    board[0] = ""
    board[1] = "" 
    board[2] = ""
    board[3] = ""
    board[4] = ""
    board[5] = ""
    board[6] = ""
    board[7] = ""
    board[8] = ""
    main()


def wino():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("win.wav"), maxtime=6000)
    winnerwin = GraphWin("winner!", 400,400)
    owintext = Text(Point(200,200),"0 wins!")
    owintext.draw(winnerwin)
    winnerwin.getMouse()
    winnerwin.close()
    board[0] = ""
    board[1] = "" 
    board[2] = ""
    board[3] = ""
    board[4] = ""
    board[5] = ""
    board[6] = ""
    board[7] = ""
    board[8] = ""
    main()



# gameplay loop   

def main():

    

# upper and lower limits for cell positions. This is to locate player click and place image in cell

    cell1top = 0
    cell1bot = 200.0
    cell1left = 0.0
    cell1right = 200.0 
    cell2top = 0
    cell2bot = 200.0
    cell2left = 200
    cell2right = 400
    cell3top = 0
    cell3bot = 200.0
    cell3left = 400
    cell3right = 600
    cell4top = 200.0
    cell4bot = 400.0
    cell4left = 0
    cell4right = 200
    cell5top = 200
    cell5bot = 400
    cell5left = 200
    cell5right = 400
    cell6top = 200
    cell6bot = 400.0
    cell6left = 400
    cell6right = 600
    cell7top = 400
    cell7bot = 600.0
    cell7left = 0
    cell7right = 200
    cell8top = 400.0
    cell8bot = 600.0
    cell8left = 200
    cell8right = 400
    cell9top = 400
    cell9bot = 600.0 
    cell9left = 400
    cell9right = 600

# place holders to see if cell is populated.
# this was implemented before the board list but decided to keep this tracking system also

    xcell1 = ""
    xcell2 = ""
    xcell3 = ""
    xcell4 = ""
    xcell5 = ""
    xcell6 = ""
    xcell7 = ""
    xcell8 = ""
    xcell9 = ""
   
# Defining the X and O image names for drawing when user selects positions "tic = X" "tac = O"
 
    x = "tic.png"  
    o = "tac.png"
   

# Game sound library

    pygame.init()
    pygame.mixer.music.load("what is love 8 bit.mp3") 
    pygame.mixer.Sound("punch.wav")
    pygame.mixer.Sound("win.wav")
   


# Game ending criteria

    turns = 0

# game view 
    
    win = GraphWin("Tic Tac Toe", 600,600)
    vertical_line1 = Line(Point(200,50),Point(200,550))
    vertical_line2 = Line(Point(400,50),Point(400,550))
    horizontal_line1 = Line(Point(50,200),Point(550,200))
    horizontal_line2 = Line(Point(50,400),Point(550,400))
    headertext = Text(Point(300,25),"Tic Tac Toe")
    headertext.setStyle("bold")
    headertext.setSize(18)
    vertical_line1.draw(win)
    vertical_line2.draw(win)
    horizontal_line1.draw(win)
    horizontal_line2.draw(win)
    headertext.draw(win)
    gamestart = Text(Point(300,575),"Click anywhere to start a game")
    gamestart.setStyle("bold")
    gamestart.setSize(24)
    gamestart.draw(win)
    win.getMouse()
    gamestart.undraw()
    pygame.mixer.music.play(2)
    pygame.mixer.music.set_volume(0.1)

  
# turns loop. Checks click region the checks if cell is available.
# If cell is available, image get placed and value of cell changes
# if cell isnt available, error window pops up and player loses current turn

   
    
    while turns < 9:


#player 1 text/prompt

        player1text = Text(Point(300,580),"Player X's turn. Click a box!")
        player1text.draw(win)
        player1text.setStyle("bold")
        player1text.setSize(24)
        a = win.getMouse()
        ycord = a.getX()
        xcord = a.getY()
        print(xcord)
        print(ycord)
        

        if xcord < cell1bot and xcord > cell1top and ycord > cell1left and ycord < cell1right and xcell1 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic1 = Image(Point(125,125), "tic.png")
            pic1.draw(win)
            xcell1 = "x"
            board[0] = "x"
            print(board)
            
        
        elif xcord < cell1bot and xcord > cell1top and ycord > cell1left and ycord < cell1right and xcell1 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn!")
            errortext.draw(errorwin)
            print(xcell1)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
          
                
        elif xcord < cell2bot and xcord > cell2top and ycord > cell2left and ycord < cell2right and xcell2 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic2 = Image(Point(300,125), "tic.png")
            pic2.draw(win)
            xcell2 = "x" 
            board[1] = "x"
            print(board)
        
        elif xcord < cell2bot and xcord > cell2top and ycord > cell2left and ycord < cell2right and xcell2 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
        elif xcord < cell3bot and xcord > cell3top and ycord > cell3left and ycord < cell3right and xcell3 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic3 = Image(Point(475,125), "tic.png")
            pic3.draw(win)
            xcell3 = "x"
            board[2] = "x"
            print(board)
        

        elif xcord < cell3bot and xcord > cell3top and ycord > cell3left and ycord < cell3right and xcell3 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
            
        elif xcord < cell4bot and xcord > cell4top and ycord > cell4left and ycord < cell4right and xcell4 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic4 = Image(Point(100,300), "tic.png")
            pic4.draw(win)
            xcell4 = "x" 
            board[3] = "x"
            print(board)
        

        elif xcord < cell4bot and xcord > cell4top and ycord > cell4left and ycord < cell4right and xcell4 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            

        elif xcord < cell5bot and xcord > cell5top and ycord > cell5left and ycord < cell5right and xcell5 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic5 = Image(Point(300,300), "tic.png")
            pic5.draw(win)
            xcell5 = "x"
            board[4] = "x"
            print(board)
        

        elif xcord < cell5bot and xcord > cell5top and ycord > cell5left and ycord < cell5right and xcell5 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell6bot and xcord > cell6top and ycord > cell6left and ycord < cell6right and xcell6 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic6 = Image(Point(500,300), "tic.png")
            pic6.draw(win)
            xcell6 = "x"
            board[5] = "x"
            print(board)
        

        elif xcord < cell6bot and xcord > cell6top and ycord > cell6left and ycord < cell6right and xcell6 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
        elif xcord < cell7bot and xcord > cell7top and ycord > cell7left and ycord < cell7right and xcell7 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic7 = Image(Point(100,500), "tic.png")
            pic7.draw(win)
            xcell7 = "x" 
            board[6] = "x"
            print(board)
        

        elif xcord < cell7bot and xcord > cell7top and ycord > cell7left and ycord < cell7right and xcell7 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell8bot and xcord > cell8top and ycord > cell8left and ycord < cell8right and xcell8 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic8 = Image(Point(300,500), "tic.png")
            pic8.draw(win)
            xcell8 = "x"
            board[7] = "x"
            print(board)
        

        elif xcord < cell8bot and xcord > cell8top and ycord > cell8left and ycord < cell8right and xcell8 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell9bot and xcord > cell9top and ycord > cell9left and ycord < cell9right and xcell9 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic9 = Image(Point(500,500), "tic.png")
            pic9.draw(win)
            xcell9 = "x" 
            board[8] = "x"
            print(board)
        

        elif xcord < cell9bot and xcord > cell9top and ycord > cell9left and ycord < cell9right and xcell9 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)

# checks win criteria 
# undraw players turn text
# accumlates turn by 1
        time.sleep(1)
        xwincriteria()
        player1text.undraw()
        turns = turns + 1

# Player 2 text/prompt        

        player2text = Text(Point(300,580),"Player O's turn. Click a box!")
        player2text.draw(win)
        player2text.setStyle("bold")
        player2text.setSize(24)
        b = win.getMouse()
        ycord = b.getX()
        xcord = b.getY()
        print(xcord)
        print(ycord)


        if xcord < cell1bot and xcord > cell1top and ycord > cell1left and ycord < cell1right and xcell1 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic1 = Image(Point(100,100), "tac.png")
            pic1.draw(win)
            xcell1 = "o"
            board[0] = "o"
            print(board)
        

        elif xcord < cell1bot and xcord > cell1top and ycord > cell1left and ycord < cell1right and xcell1 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)

             
        elif xcord < cell2bot and xcord > cell2top and ycord > cell2left and ycord < cell2right and xcell2 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic2 = Image(Point(300,100), "tac.png")
            pic2.draw(win)
            xcell2 = "o" 
            board[1] = "o"
            print(board)

        elif xcord < cell2bot and xcord > cell2top and ycord > cell2left and ycord < cell2right and xcell2 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
            
        elif xcord < cell3bot and xcord > cell3top and ycord > cell3left and ycord < cell3right and xcell3 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic3 = Image(Point(500,100), "tac.png")
            pic3.draw(win)
            xcell3 = "o" 
            board[2] = "o"
            print(board)

        elif xcord < cell3bot and xcord > cell3top and ycord > cell3left and ycord < cell3right and xcell3 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
        elif xcord < cell4bot and xcord > cell4top and ycord > cell4left and ycord < cell4right and xcell4 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic4 = Image(Point(100,300), "tac.png")
            pic4.draw(win)
            xcell4 = "o" 
            board[3] = "o"
            print(board)

        elif xcord < cell4bot and xcord > cell4top and ycord > cell4left and ycord < cell4right and xcell4 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)

        elif xcord < cell5bot and xcord > cell5top and ycord > cell5left and ycord < cell5right and xcell5 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic5 = Image(Point(300,300), "tac.png")
            pic5.draw(win)
            xcell5 = "o" 
            board[4] = "o"
            print(board)

        elif xcord < cell5bot and xcord > cell5top and ycord > cell5left and ycord < cell5right and xcell5 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell6bot and xcord > cell6top and ycord > cell6left and ycord < cell6right and xcell6 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic6 = Image(Point(500,300), "tac.png")
            pic6.draw(win)
            xcell6 = "o" 
            board[5] = "o"
            print(board)

        elif xcord < cell6bot and xcord > cell6top and ycord > cell6left and ycord < cell6right and xcell6 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
            
        elif xcord < cell7bot and xcord > cell7top and ycord > cell7left and ycord < cell7right and xcell7 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic7 = Image(Point(100,500), "tac.png")
            pic7.draw(win)
            xcell7 = "o" 
            board[6] = "o"
            print(board)

        elif xcord < cell7bot and xcord > cell7top and ycord > cell7left and ycord < cell7right and xcell7 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell8bot and xcord > cell8top and ycord > cell8left and ycord < cell8right and xcell8 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic8 = Image(Point(300,500), "tac.png")
            pic8.draw(win)
            xcell8 = "o" 
            board[7] = "o"
            print(board)

        elif xcord < cell8bot and xcord > cell8top and ycord > cell8left and ycord < cell8right and xcell8 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)
                
        elif xcord < cell9bot and xcord > cell9top and ycord > cell9left and ycord < cell9right and xcell9 == "":
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("punch.wav"), maxtime=675)
            pic9 = Image(Point(500,500), "tac.png")
            pic9.draw(win)
            xcell9 = "o"
            board[8] = "o"
            print(board)

        elif xcord < cell9bot and xcord > cell9top and ycord > cell9left and ycord < cell9right and xcell9 != "":
            errorwin = GraphWin("Oops", 300,300)
            errortext = Text(Point(150,150), "Cell occupied, you lose a turn, idiot!")
            errortext.draw(errorwin)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("denied.wav"), maxtime=2000)

# checks win criteria 
# undraw players turn text
# accumlates turn by 1

        time.sleep(1)
        owincriteria()
        player2text.undraw()
        turns = turns + 1
           

main()



