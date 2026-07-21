from time import sleep
from random import randint

tic_tac = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

print("\n" + "=" * 40)
print("      WELCOME TO TIC-TAC-TOE!      ")
print("=" * 40)

def check_game_status(): #FIX ME: See if its worth it
    pass

def instructions():
    print("=" * 40)
    print(" Instructions:")
    print(" • The board uses ROW and COLUMN coordinates.")
    print(" • Both rows and columns range from \033[33m0 to 2\033[m.")
    print(" • Example: Row 0 and Column 0 is the top-left corner.")
    print(" • Player 1 is \033[34m'X'\033[m and Player 2 is \033[34m'O'\033[m.")
    print("=" * 40 + "\n")


def print_tic_tac():
    print()
    for position, list_tic_tac in enumerate(tic_tac):
        for index, character in enumerate(list_tic_tac):
            if index == 1:
                print(f'|{character}|', end='')
            else:
                print(character, end='')
        if position != 2:
            print('\n-----')
        else:
            print('\n')


def validate_tie():
    for line in range(3):
        for column in range(3):
            if tic_tac[line][column] == ' ':
                return False
    return True


def validate_horizontal():
    for line in range(3):
        horizontal_x = 0
        horizontal_o = 0
        for column in range(3):
            if tic_tac[line][column] == 'X':
                horizontal_x += 1
            if tic_tac[line][column] == 'O':
                horizontal_o += 1
            if horizontal_x == 3 or horizontal_o == 3:
                return True
    return False


def validate_vertical():
    for column in range(3): # static_index
        vertical_x = 0
        vertical_o = 0
        for line in range(3): #volatile_index
            if tic_tac[line][column] == 'X':
                vertical_x += 1
            if tic_tac[line][column] == 'O':
                vertical_o += 1
            if vertical_x == 3 or vertical_o == 3:
                return True
    return False


def validate_diagonal_right():
    """Validates a diagonal tic-tac-toe win (down right to up left)"""
    diagonal_right_x = 0
    diagonal_right_o = 0
    for index in range(3):
        if tic_tac[index][index] == 'X':
            diagonal_right_x += 1
        if tic_tac[index][index] == 'O':
            diagonal_right_o += 1
        if diagonal_right_x == 3 or diagonal_right_o == 3:
            return True
    return False


def validate_diagonal_left():
    """Validates a diagonal tic-tac-toe win (down left to up right)"""
    line = 0
    column = 2
    diagonal_left_x = 0
    diagonal_left_o = 0
    for rounds in range(3):
        if tic_tac[line][column] == 'X':
            diagonal_left_x += 1
        if tic_tac[line][column] == 'O':
            diagonal_left_o += 1
        if diagonal_left_x == 3 or diagonal_left_o == 3:
            return True
        line += 1
        column -= 1
    return False


def coop_game():
  while True:
    print_tic_tac()

    try:
        line = int(input('Which row do you want to mark an \033[34m\'X\'\033[m? '))
        column = int(input('Which column do you want to mark an \033[34m\'X\'\033[m? '))
    except ValueError:
        print('\033[31mERROR! CHOOSE VALID VALUES ONLY!\033[m')
        continue
    if ' ' in tic_tac[line][column]:
        tic_tac[line][column] = 'X'
    else:
        print('\033[31mPosition already marked! choose other!\033[m')
        continue

    print_tic_tac()
    horizontal = validate_horizontal()
    vertical = validate_vertical()
    diagonal_right = validate_diagonal_right()
    diagonal_left = validate_diagonal_left()
    tie = validate_tie()

    if horizontal or vertical or diagonal_right or diagonal_left: # X wins
        return print('Congratulations X!! What an amazing win!')
    # FIX ME: Better congrats message
    if tie:
        return print('It\'s a TIE!!!')
    # FIX ME: Better congrats message

    try:
        line = int(input('Which row do you want to mark an \033[34m\'O\'\033[m? '))
        column = int(input('Which column do you want to mark an \033[34m\'O\'\033[m? '))
    except ValueError:
        print('\033[31mERROR! CHOOSE VALID VALUES ONLY!\033[m')
        continue
    if ' ' in tic_tac[line][column]:
        tic_tac[line][column] = 'O'
    else:
        print('\033[31mPosition already marked! choose other!\033[m')
        continue

    print_tic_tac()
    horizontal = validate_horizontal()
    vertical = validate_vertical()
    diagonal_right = validate_diagonal_right()
    diagonal_left = validate_diagonal_left()
    tie = validate_tie()

    if horizontal or vertical or diagonal_right or diagonal_left:  # Y wins
        return print('Congratulations Y!! What an amazing win!')
    # FIX ME: Better congrats message
    if tie:
        return print('It\'s a TIE!!!')


def ai_game():
    while True:
        print_tic_tac()
        try:
            line = int(input('Which row do you want to mark an \033[34m\'X\'\033[m? '))
            column = int(input('Which column do you want to mark an \033[34m\'X\'\033[m? '))
        except ValueError:
            print('\033[31mERROR! CHOOSE VALID VALUES ONLY!\033[m')
            continue
        if ' ' in tic_tac[line][column]:
            tic_tac[line][column] = 'X'
        else:
            print('\033[31mPosition already marked! choose other!\033[m')
            continue

        horizontal = validate_horizontal()
        vertical = validate_vertical()
        diagonal_right = validate_diagonal_right()
        diagonal_left = validate_diagonal_left()
        tie = validate_tie()

        if horizontal or vertical or diagonal_right or diagonal_left:  # X wins
            return print('Congratulations X!! What an amazing win!')
            # FIX ME: Better congrats message
        if tie:
            return print('It\'s a TIE!!!')

        while True:
            random_line = randint(0, 2)
            random_column = randint(0, 2)
            if tic_tac[random_line][random_column] != ' ':
                tic_tac[random_line][random_column] = 'O'
                break

        horizontal = validate_horizontal()
        vertical = validate_vertical()
        diagonal_right = validate_diagonal_right()
        diagonal_left = validate_diagonal_left()
        tie = validate_tie()

        if horizontal or vertical or diagonal_right or diagonal_left:  # AI wins
            return print('AI beat you!')
        if tie:
            return print('It\'s a TIE!!!')


while True:
    print('Menu:')
    print('\t1: Instructions')
    print('\t2: Play against player')
    print('\t3: Play against A.I')
    print('\t4: Exit')
    try:
        option = int(input('Choose an option: '))
    except ValueError:
        print('\033[31mUSE VALID OPTIONS ONLY!\033[m')
        continue
    if option == 1:
        instructions()
        sleep(5)
    elif option == 2:
        print('Play against player')
        coop_game()
        tic_tac = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    elif option == 3:
        print('Play against A.I')
        ai_game()
        tic_tac = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    elif option == 4:
        break
    else:
        print('\033[1;31mInvalid Value! Select again\033[m')