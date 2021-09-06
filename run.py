from random import randint

#set up game board
board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ").join(row)

#code to add battleships to game board
def random_row(board):
  return randint(0, len(board) -1)

def random_column(board):
  return randint(0, len(board) -1)

ship_row = random_row(board)
ship_col = random_column(board)

#code to prompt user to guess row and allow input
guess_row = int(input("Guess row: "))