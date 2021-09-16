from random import randint
import logging

# welcome message
print("Welcome to Battleships.")
username = input("What is your name? ")
# print("Username is: " + username)

# set up game board
# print("Computer")
computer_board = []
computer_board_with_ships = []

for x in range(5):
    computer_board.append(["O"] * 5)
    computer_board_with_ships.append(["O"] * 5)


def print_computer_board(computer_board):
    for i in computer_board:
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
    return randint(0, len(player_board[0]) - 1)


# set battleships for player board
for x in range(3):
    while True:
        player_row = random_row(player_board)
        player_col = random_column(player_board)
        if player_board[player_row][player_col] == "@":
            continue
        else:
            player_board[player_row][player_col] = "@"


# print_board(player_board)
# print(score_message)

# code to add battleships to computer board
for x in range(3):
    ship_row = random_row(computer_board)
    ship_col = random_column(computer_board)

    computer_board_with_ships[ship_row][ship_col] = "@"


# code to count number of turns, invite user input, validate user input and give outcomes
for turn in range(9):
    print("Computer")
    print_computer_board(computer_board)
    print(username)
    print_board(player_board)
    print(score_message)

    print("SHIP ROW: ", ship_row)
    print("SHIP COLUMN: ", ship_col)
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

    if computer_board_with_ships[guess_row][guess_column] == "@":
        computer_board_with_ships[guess_row][guess_column] = "X"
        computer_board[guess_row][guess_column] = "X"
        print("Direct hit! You sank the computer's battleship!")
        your_score += 1
        score_message = (f"Your score: {your_score} Computer's score: {comp_score} ")
        print(score_message)
    else:
        print("Nice try! You missed the computer's battleship!")
        computer_board[guess_row][guess_column] = "X"
        # print(f"My ship was at {ship_row, ship_col}.")

    # code to enable computer guess
    computer_guess_row = randint(0, 4)
    computer_guess_column = randint(0, 4)
    print(f"Computer guessed: {computer_guess_row, computer_guess_column}")
    # outcome of computer's guess
    if player_board[computer_guess_row][computer_guess_column] == "@":
        player_board[computer_guess_row][computer_guess_column] = "X"
        print("Ha ha! Bow to me, human! I sunk your battleship")
        player_board[player_row][player_col] = "X"
        comp_score += 1
        score_message = (
            f"Your score: {your_score} Computer's score: {comp_score} "
        )
        print(score_message)
    else:
        print("You're lucky I missed, human!")
        player_board[computer_guess_row][computer_guess_column] = "X"
    if turn == 8 or (comp_score == 3 and your_score < 3):
        print("Game Over")
    turn = 1
    if your_score == 3:
        print("You win!")
        break
    if comp_score == 3:
        print("You lose!")
        break
