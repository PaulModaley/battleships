from random import randint

# set up game board
print("Computer")
board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for i in board:
        print((" ").join(i))

print_board(board)


#set up human player board
print("You")
player_board = []

for x in range(5):
    player_board.append(["O"] * 5)

def print_board(player_board):
    for i in player_board:
        print((" ").join(i))

print_board(player_board)

# code to add battleships to computer board
def random_row(board):
    return randint(0, len(board) - 1)


def random_column(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_column(board)

#code to add battleships to player board
def random_row(player_board):
    return randint(0, len(player_board) - 1)

def random_column(player_board):
    return randint(0, len(player_board) - 1)

player_row = random_row(board)
player_col = random_column(board)

# code to prompt user to guess row and allow input
guess_row = int(input("Guess row (maximum is 5): "))
guess_column = int(input("Guess column (maximum is 5): "))

print(ship_row)
print(ship_col)

# outcome of user's guess
if guess_row == ship_row and guess_column == ship_col:
    print("Direct hit! You sank my battleship!")
else:
    print("Nice try! You missed my battleship!")
    board[guess_row][guess_column] = "X"
    print_board(board)
    