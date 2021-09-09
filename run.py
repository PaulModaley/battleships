from random import randint

#welcome message
print("Welcome to Battleships.")
username = input("What is your name? ")
print("Username is: " + username)


# set up game board
print("Computer")
board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for i in board:
        print((" ").join(i))

print_board(board)


#set up human player board and add battleships to player board
print(username)
player_board = []

for x in range(5):
    player_board.append(["O"] * 5)

def print_board(player_board):
    for i in player_board:
        print((" ").join(i))

def random_row(player_board):
    return randint(0, len(player_board) - 1)

def random_column(player_board):
    return randint(0, len(player_board) - 1)

player_row = random_row(board)
player_col = random_column(board)

player_board[player_col][player_row] = "@"        

print_board(player_board)

# code to add battleships to computer board
def random_row(board):
    return randint(0, len(board) - 1)


def random_column(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_column(board)

#turns
for turn in range(9):
    guess_row = int(input("Guess row (Enter number 0-4): "))
    guess_column = int(input("Guess column (Enter number 0-4): "))
        
    if guess_row == ship_row and guess_column == ship_col:
        print("Direct hit! You sank my battleship!")
    else:
        print("Nice try! You missed my battleship!")
        print(f"My ship was at {ship_row, ship_col}.")
        board[guess_row][guess_column] = "X"
        print_board(board)

#code to enable computer guess
    computer_guess_row = randint(0, 5)
    computer_guess_column = randint(0, 5)
    print(f"Computer guessed: {computer_guess_row, computer_guess_column}")

#outcome of computer's guess
    if computer_guess_row == player_row and computer_guess_column == player_col:
        print("Ha ha! Bow to me, human! I sunk your battleship")
    else:
        print("You're lucky I missed, human!")
    if turn == 8:
        print("Game Over")
    turn =+ 1
    