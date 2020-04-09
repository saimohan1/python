#!/usr/bin/python
# Basic Implementation of TIC TAC TOE Game
# Auther - L Saimohan Rao
# Email  - saimohanrao92@gmail.com


# Tic Tac Toe Game board
board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

player1 = ""        # Name of the player 1
player2 = ""        # Name of the player 2
used_numbers = []   # List is used to store used inputs
invalid_input = 0   # Used to validate number of invalid inputs


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def get_players_info():
    """
        This Function is used to get the player names.
    """
    global player1, player2
    player1 = input("Please enter the first player name: ")
    print("{} will play as 'X'".format(player1.capitalize()))
    player2 = input("Please enter the Second player name: ")
    print("{} will play as 'O'".format(player2.capitalize()))


def is_win(code):
    """
    This function used to check, who won
        1. checks for all rows
        2. Checks for all column
        3. Checks for diagonal

    :param code:
        X or O
    :return:
        True if won or tie.
        False if no won or tie.
    """
    global board
    if (board[0] == board[1] == board[2] == code or
            board[3] == board[4] == board[5] == code or
            board[6] == board[7] == board[8] == code):
        return True
    elif (board[0] == board[3] == board[6] == code or
          board[1] == board[4] == board[7] == code or
          board[2] == board[5] == board[8] == code):
        return True
    elif (board[0] == board[4] == board[8] == code or
          board[2] == board[4] == board[6] == code):
        return True
    else:
        return False


def check_win():
    """
        This function is used to check, if
        1. Player1 is won or
        2. Player2 is won or
        3. Match tied
    :return:
        Returns Player name
    """
    global used_numbers
    if is_win("X"):
        display_board()
        print("Congratulation %s !!!! You Won the Game." % player1.capitalize())
        return player1
    elif is_win("O"):
        display_board()
        print("Congratulation %s !!!! You Won the Game" % player2.capitalize())
        return player2
    elif len(used_numbers) == 9:
        display_board()
        print("Match TIED. Congratulations both %s and %s." %(player1, player2))
        return player1 + player2
    else:
        return None


def validate_input(user_input):
    """
        This function is used to validate the user entered input.
    :param user_input:
        user_input :- User entered input.
    :return:
        Valid if input is between 0 - 9.
        Invalid for other.
    """
    global used_numbers
    if user_input < 0 or user_input > 9 or user_input in used_numbers:
        return "Invalid"
    else:
        used_numbers.append(user_input)
        return "Valid"


def get_input(player):
    """
        This Function is used to get the user input.
    :param player:
        player :- For which player input is taking.
    :return:
        Return valid user input.
        Terminate game if invalid input entered.
    """
    global invalid_input
    try:
        while invalid_input < 3:
            user_input = int(input("%s Please select your input: " % str(player).capitalize()))
            if validate_input(user_input) != "Valid":
                print("Please Enter valid input.. Try Again")
                invalid_input += 1
            else:
                invalid_input = 0
                return user_input
        else:
            print("Maximum Retry exceeded. Quiting Game.")
            exit(1)
    except ValueError:
        print("Did not Entered any input!!. Please Restart Game.")
        exit(1)


def start_the_game():
    """
        This is the main function for the game.
    :return:
        Nothing
    """
    global player1, player2, board
    get_players_info()
    while True:
        display_board()
        # First players inpur
        user_input = get_input(player1)
        board[user_input] = 'X'
        if check_win() is not None:
            print("Game Over...")
            break
        display_board()
        user_input = get_input(player2)
        board[user_input] = 'O'
        if check_win() is not None:
            print("Game Over...")
            break


if __name__ == '__main__':
    print("#" * 35)
    print("#" * 11 + " TIC TAC TOE " + "#" * 11)
    print("#" * 35)
    start_the_game()

