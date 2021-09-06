from random import randint

# set up game board
board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for i in board:
        print((" ").join(i))

print_board(board)

# code to add battleships to game board
def random_row(board):
    return randint(0, len(board) - 1)


def random_column(board):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_column(board)

# code to prompt user to guess row and allow input
guess_row = int(input("Guess row: "))
guess_column = int(input("Guess column: "))

print(ship_row)
print(ship_col)

# outcome of user's guess
if guess_row == ship_row and guess_column == ship_col:
    print("Direct hit! You sank my battleship!")
else:
    print("Nice try! You missed my battleship!")
    board[guess_row][guess_column] = "X"
    print_board(board)
