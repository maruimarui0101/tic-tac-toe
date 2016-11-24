import random

board = [" "]*10

# BOARD DISPLAY

def board_display(): 
    print("\n")

    print("|" + " " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] + " " + "|")
    print("_____________")
    print("|" + " " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] + " " + "|")
    print("_____________")
    print("|" + " " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] + " " + "|")
 
    print("\n")

# SPACE CHECK

def space_check(board, position):
    return board[position] == " " # is this space empty

# BOARD FULL CHECK

def board_check (board):
    for i in range(1,10):
        if space_check(board, i):
            return False # spaces full
    return True # board full

# WIN CHECK

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# WHO HAS THE FIRST MOVE? [WORKS]

def first_turn():
    decider = random.randint(1,2)
    if decider == 1:
        turn = "Player 1"
    else:
        turn = "Player 2"
    print("{} has the first move!\n".format(turn))

    print("Player 1: O")
    print("Player 2: X")

    return turn


# ARE THE PLAYERS READY? [WORKS]

print("Welcome to Tic Tac Toe")
ready_start = input("Are you ready to start? (y/n): ")

while ready_start.lower() != "y" or "n":
    if ready_start.lower() == "y":
        print("glhf")
        game_on = True
        turn = first_turn()
        break
    elif ready_start.lower() == "n":
        game_on = False
        break
    else:
        print("That is not a valid response. Please try again!")
        ready_start = input("Are you ready to start? (y/n)")




player1_marker = "O"
player2_marker = "X"


while game_on:

    while not board_check(board):

        # PLAYER 1

        if turn == "Player 1":        
            board_display()

            choice = int(input("Please indicate your desired position: ")) # note input() assumes str input
            while choice != [1,2,3,4,5,6,7,8,9]:
                if 1 <= choice <= 9:
                    if space_check(board, choice):
                        board[choice] = player1_marker
                        break
                    else:
                        print("Space is occupied, please pick another!")
                        choice = int(input("Please indicate your desired position: "))
                else:
                    print("Invalid!")
                    choice = int(input("Please indicate your desired position: "))

            if win_check(board, player1_marker):
                print("gg %r wins!"%(turn))  
                board_display()
                game_on = False
                break 
            else:
                print("continuing...")
                turn = "Player 2"
                
        # PLAYER 2

        else:
            board_display()

            choice = int(input("Please indicate your desired position: ")) # note input() assumes str input
            while choice != [1,2,3,4,5,6,7,8,9]:
                if 1 <= choice <= 9:
                    if space_check(board, choice):
                        board[choice] = player2_marker
                        break
                    else:
                        print("Space is occupied, please pick another!")
                        choice = int(input("Please indicate your desired position: "))
                else:
                    print("Invalid!")
                    choice = int(input("Please indicate your desired position: "))

            if win_check(board, player2_marker):
                print("gg %r wins!"%(turn))  
                board_display()
                game_on = False
                break
                
            else:
                print("continuing...")
                turn = "Player 1"

        if board_check(board):
            print("Game has tied")
            game_on = False

if not game_on:
    print("Have a nice day!")


    
    


