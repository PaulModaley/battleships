from random import randint
import logging

# welcome message
print("Welcome to Battleships.")
username = input("What is your name? ")
# print("Username is: " + username)

# set up game board
# print("Computer")
board = []

for x in range(5):
    board.append(["O"] * 5)


def print_computer_board(board):
    for i in board:
        print((" ").join(i))


# print_computer_board(board)

# scoring
your_score = 0

comp_score = 0
score_message = (f"Your score: {your_score} " f" Computer's score: {comp_score} ")


# set up human player board and add battleships to player board
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

for x in range(3):
    player_row = random_row(board)
    player_col = random_column(board)

    player_board[player_row][player_col] = "@"

# print_board(player_board)
# print(score_message)

# code to add battleships to computer board
for x in range(3):
    ship_row = random_row(board)
    ship_col = random_column(board)

# code to count number of turns, invite user input, validate user input and give outcomes
for turn in range(9):
    print("Computer")
    print_computer_board(board)
    print(username)
    print_board(player_board)
    print(score_message)
    while True:
        try:
            guess_row = int(input("Guess row (Enter number 1-5): "))
            guess_column = int(input("Guess column (Enter number 1-5): "))
            if guess_row in [1, 2, 3, 4, 5] \
                and guess_column in [1, 2, 3, 4, 5]:
                guess_row = guess_row - 1
                guess_column = guess_column - 1
                break
            else:
                print("Invalid input\n")
        except Exception as ex:
            print("Invalid input\n")
            logging.info(ex)
            continue

    if guess_row == ship_row and guess_column == ship_col:
        print("Direct hit! You sank my battleship!")
        your_score += 1
        print(score_message)
    else:
        print("Nice try! You missed my battleship!")
        board[guess_row][guess_column] = "X"
        # print(f"My ship was at {ship_row, ship_col}.")

    # code to enable computer guess
    computer_guess_row = randint(0, 5)
    computer_guess_column = randint(0, 5)
    print(f"Computer guessed: {computer_guess_row, computer_guess_column}")

    # outcome of computer's guess
    if computer_guess_row == player_row and computer_guess_column == player_col:
        print("Ha ha! Bow to me, human! I sunk your battleship")
        comp_score += 1
        print(score_message)
    else:
        print("You're lucky I missed, human!")
    if turn == 8:
        print("Game Over")
    turn = 1
