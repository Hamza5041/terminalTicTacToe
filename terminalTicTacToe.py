import os
import time

# This function checks each possiblility of a win and returns true if there is one
# the player is either an X or 
def checkWin(bd, player):
    #check 1st row
    if (player == bd[0][0] == bd[0][1]  == bd[0][2]):
        return True
    #second row
    elif (player == bd[1][0] == bd[1][1]  == bd[1][2]):
        return True
    #3rd row
    elif (player == bd[2][0] == bd[2][1]  == bd[2][2]):
        return True

    #check 1st column
    elif (player == bd[0][0] == bd[1][0]  == bd[2][0]):
        return True
    #2nd column
    elif (player == bd[0][1] == bd[1][1]  == bd[2][1]):
        return True
    #3rd colum
    elif (player == bd[0][2] == bd[1][2]  == bd[2][2]):
        return True

    #check diag1 l to r
    elif (player == bd[0][0] == bd[1][1]  == bd[2][2]):
        return True

    #check diag2 r to left
    elif (player == bd[2][0] == bd[1][1]  == bd[0][2]):
        return True

    return False

def printBoard(bd):
    os.system("cls")

    #Code from chat gpt.  Used to pretty print the board and make it look nice
    for i, row in enumerate(bd):
        print(" | ".join(cell if cell else " " for cell in row))
        if i < len(bd) - 1:
            print("-" * (len(row) * 4 - 3))

    print("")

# start of game
os.system("cls")
print("Welcome to tik tac toe!")
print("")
print("-Simply enter the row number and position when asked (1,2,3)")
print("")
print("Enjoy :)")
print("")

# get player names
player1 = input("Player1 enter your name: ")
print("X is: " + player1)

player2 = input("Player2 enter your name: ")
print("O is: " + player2)

#array to hold the board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

# turn will alternate between players until end of game. hence denoting whos turn it is
turn = player1
round = 1

# loop will run until there is no space left on board or there is win
while(round <= 9):
    printBoard(board)

    # Value is either X or O depending on what players turn it is
    value = lambda val: "X" if val==player1 else "O"
    print("It is " + turn + "'s turn.  You are: "+ value(turn))

    # Ask player what row they want to play
    # if they put number larger than 3, put error message and skip loop iteration
    row = int(input(turn + " what row would you like to play: "))
    if (row > 3):
        print("Please enter a row number (either 1, 2, or 3)")
        time.sleep(6)
        continue

    # For printing st nd or rd depending on what row was chosen
    suffix = lambda x: "st" if x==1 else "nd" if x==2 else "rd"


    print("")
    # get position in row player wants to play
    # again, if larger than 3, put error message and try again
    print("if you would like to change what row to play, enter -1.")
    index = int(input("where in the "+ str(row) + suffix(row) + " row would you like to play: "))

    if (index > 3):
        print("Please enter a valid place in the row (either 1, 2, or 3)")
        time.sleep(6)
        continue

    # -1 index is if player chose wrong row to play
    if(index == -1):
        continue

    # First check to see if the spot has not been taken yes
    # if it has put error message and try again
    if (board[row-1][index-1] != ""):
        print ("")
        print("Sorry " + turn +  ", this spot is taken. Try again")

        time.sleep(6)
        
        continue

    # place either an X or O depending on whos turn it is.
    # after placing, check for a win.  In which case end the while loop
    # if no win, change the turn to opposite playeer and increment the turncounter
    if (turn == player1):
        board[row-1][index-1] = "X"

        if (checkWin(board, "X")):
            break
        turn = player2

    else:
        board[row-1][index-1] = "O"

        if (checkWin(board, "O")):
            break

        turn = player1

    round+=1

printBoard(board)

# after the end of the while loop, if it got to the 10th round (9 playes)
# then there was no winner and all spots have been used
if (round == 10):
    print("It is a tie!")
# otherwise, whosever turn it was last, won
else:
    print(turn + " WINS!")    