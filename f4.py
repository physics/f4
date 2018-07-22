# imports what allows f4 to terminate
import sys

# the lists that make up the board
line1 = ['-', '-', '-', '-', '-', '-', '-']
space1 = '\n'
line2 = ['-', '-', '-', '-', '-', '-', '-']
space2 = '\n'
line3 = ['-', '-', '-', '-', '-', '-', '-']
space3 = '\n'
line4 = ['-', '-', '-', '-', '-', '-', '-']
space4 = '\n'
line5 = ['-', '-', '-', '-', '-', '-', '-']
space5 = '\n'
line6 = ['-', '-', '-', '-', '-', '-', '-']
board = [line1, space1, line2, space2, line3, space3, line4, space4, line5, space5, line6]

# a concatenated version of the parts of the board
pboard = str(board[0])+str(board[1])+str(board[2])+str(board[3])+str(board[4])+str(board[5])+str(board[6])+str(board[7])+str(board[8])+str(board[9])+str(board[10])

# displays the board as well as numbers on top of the board
print('  1    2    3    4    5    6    7\n' + pboard)

# sets what the current player is, used when printing who won the game
xp = 'x'

# all the checks that are run every move to see if a player has won yet
def check(xp):
    
            # checks for horizontal winning in the first 4 columns     
            for e in range(0,11,2):
                for i in range(0,4):
                    if(board[e][i] == xp and board[e][i+1] == xp and board[e][i+2] == xp and board[e][i+3] == xp):
                        print("Player " + xp.upper() + " has taken the trophy. ?? ")
                        sys.exit()
                    
            # checks for vertical winning in the first 4 columns starting from the top line, going down
            for i in range(0,4):
                if(board[0][i] == xp and board[0+2][i] == xp and board[0+4][i] == xp and board[0+6][i] == xp):
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                
            # checks for vertical winning in all 7 columns starting from the bottom line, going up
            for i in range(0,7):
                if(board[10][i] == xp and board[10-2][i] == xp and board[10-4][i] == xp and board[10-6][i] == xp):
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
            
            # checks for vertical winning starting from line 3 going down
            for i in range(0,7):
                if(board[2][i] == xp and board[2+2][i] == xp and board[2+4][i] == xp and board[2+6][i] == xp):
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                    
            # checks diagonal winning from line one down and to the right
            for i in range(0,4):
                if board[0][i] == xp and board[0+2][i+1] == xp and board[0+4][i+2] == xp and board[0+6][i+3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                            
            # checks diagonal winning from line 6 up and to the left
            for i in range(3,7):
                if board[10][i] == xp and board[10-2][i-1] == xp and board[10-4][i-2] == xp and board[10-6][i-3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                    
            # checks diagonal winning from line 3 down and to the right
            for i in range(0,4):
                if board[2][i] == xp and board[2+2][i+1] == xp and board[2+4][i+2] == xp and board[2+6][i+3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
            
            # checks diagonal winning from line 1 down and to the left
            for i in range(3,7):
                if board[0][i] == xp and board[0+2][i-1] == xp and board[0+4][i-2] == xp and board[0+6][i-3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                    
            # checks diagonal winning from line 3 down and to the left
            for i in range(3,7):
                if board[2][i] == xp and board[2+2][i-1] == xp and board[2+4][i-2] == xp and board[2+6][i-3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                    
            # checks diagonal winning from line 6 up and to the right
            for i in range(0,4):
                if board[10][i] == xp and board[10-2][i+1] == xp and board[10-4][i+2] == xp and board[10-6][i+3] == xp:
                    print("Player " + xp.upper() + " has taken the trophy. ?? ")
                    sys.exit()
                    
            # checks for a draw
            if '-' not in board[10] and '-' not in board[8] and '-' not in board[6] and '-'not in board[4] and '-' not in board[2] and '-' not in board[0]:
                print("It is a draw.")
                sys.exit()
               
# used when player O moves, prints the board, sets the current player to O, checks for a win, and lets player X move     
def p1check(x):
    pboard = str(board[0])+str(board[1])+str(board[2])+str(board[3])+str(board[4])+str(board[5])+str(board[6])+str(board[7])+str(board[8])+str(board[9])+str(board[10])
    print('  1    2    3    4    5    6    7\n' + pboard)
    xp = 'o'
    check(xp)
    playerMoveFirst()
 
# used when player X moves, prints the board, sets the current player to X, checks for a win, and lets player O move   
def p2check(x):
    pboard = str(board[0])+str(board[1])+str(board[2])+str(board[3])+str(board[4])+str(board[5])+str(board[6])+str(board[7])+str(board[8])+str(board[9])+str(board[10])
    print('  1    2    3    4    5    6    7\n' + pboard)
    xp = 'x'
    check(xp)
    playerMoveSecond()
      
# function that starts the game, allows the first player [X] to make his move
def playerMoveFirst():
    # prompts the player to pick a column, records his input
    playerMove = input("Which column would you like to go to? Your choices are 1-7. ")
    # sets his input into the variable xp and converts it to an integer
    
    # if a player doesn't go 1-7, it repeats the game until they do
    if playerMove != "1" and playerMove != "2" and playerMove != "3" and playerMove != "4" and playerMove != "5" and playerMove != "6" and playerMove != "7":
        print("Please enter a number 1-7. ")
        playerMoveFirst()
       
    # if a player does go 1-7, it converts their input to an integer and the rest of the code runs
    else:
        x = int(playerMove)
        
    if x == x:

        # this for loop lets players move, and it checks whether they win (each move)
        for i in range(0,11,2):
            if line6[x-1] == '-':
                line6[x-1] = 'x'
                p2check(x)
            elif line5[x-1] == '-':
                line5[x-1] = 'x'
                p2check(x)
            elif line4[x-1] == '-':
                line4[x-1] = 'x'
                p2check(x)
            elif line3[x-1] == '-':
                line3[x-1] = 'x'
                p2check(x)
            elif line2[x-1] == '-':
                line2[x-1] = 'x'
                p2check(x)
            elif line1[x-1] == '-':
                line1[x-1] = 'x'
                p2check(x)
            else:

                # this function lets players pick a column if the one they picked is full
                def columnFulle():
                    print("\nPlease pick a different column, column " + str(playerMove) + " is already full.\n")
                    playerMoveFirst()
                columnFulle()

            # this line is used just so that the variable i does not remain unused
            i = str(i)

# function that initiates the second player's move
def playerMoveSecond():
    playerMove = input("Which column would you like to go to? Your choices are 1-7. ")
    
    # if a player doesn't go 1-7, it repeats the game until they do
    if playerMove != "1" and playerMove != "2" and playerMove != "3" and playerMove != "4" and playerMove != "5" and playerMove != "6" and playerMove != "7":
        print("Please enter a number 1-7. ")
        playerMoveFirst()
       
    # if a player does go 1-7, it converts their input to an integer and the rest of the code runs
    else:
        x = int(playerMove)
    
    if x == x:

        # this for loop lets players move, and it checks whether they win (each move)
        for i in range(0,11,2):
            if line6[x-1] == '-':
                line6[x-1] = 'o'
                p1check(x)
            elif line5[x-1] == '-':
                line5[x-1] = 'o'
                p1check(x)
            elif line4[x-1] == '-':
                line4[x-1] = 'o'
                p1check(x)
            elif line3[x-1] == '-':
                line3[x-1] = 'o'
                p1check(x)
            elif line2[x-1] == '-':
                line2[x-1] = 'o'
                p1check(x)
            elif line1[x-1] == '-':
                line1[x-1] = 'o'
                p1check(x)
            else:

                # this function lets players pick a column if the one they picked is full
                def columnFulle():
                    print("\nPlease pick a different column, column " + str(playerMove) + " is already full.\n")
                    playerMoveSecond()
                columnFulle()

            # this line is used just so that the variable i does not remain unused
            i = str(i)
        
# this line starts the game and lets player one move
playerMoveFirst()