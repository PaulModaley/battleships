from random import randint

#initializing board
board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ").join(row)

print(board)