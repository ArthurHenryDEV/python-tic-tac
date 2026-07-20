tic_tac = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
def coop_game():
    counter = 0
    print()
    for index in tic_tac:
            for character in index:
                if counter == 1:
                    print(f'|{character}|', end='')
                else:
                    print(character, end='')
                counter += 1
                if counter == 3:
                    print('\n-----')
                    counter = 0


option = 0
while True:
    print('Menu:')
    print('\t1: Instructions')
    print('\t2: Play against player')
    print('\t3: Play against A.I')
    print('\t4: Exit')
    option = int(input('Choose an option: '))
    if option == 1:
        print('Instructions a lot')
        # FIX ME
    elif option == 2:
        print('Play against player')
        coop_game()
    elif option == 3:
        print('Play against A.I')
        # FIX ME
    elif option == 4:
        break
    else:
        print('\033[1;31mInvalid Value! Select again')