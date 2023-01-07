
def print_board(a):
    for i in range(3):
        for j in range(3):
            print(f'{a[i][j]} ', end='')
        print('\n')
    print('\n')


def is_winner(a):
    if a[0][0] == a[1][1] and a[1][1] == a[2][2] and a[0][0] != '-':
        print(f'{a[0][0]} is the winner')
        return True
    if a[0][2] == a[1][1] and a[1][1] == a[2][0] and a[2][0] != '-':
        print(f'{a[0][2]} is the winner')
        return True
    if a[0][0] == a[0][1] and a[0][1] == a[0][2] and a[0][0] != '-':
        print(f'{a[0][0]} is the winner')
        return True
    if a[1][0] == a[1][1] and a[1][1] == a[1][2] and a[1][0] != '-':
        print(f'{a[1][0]} is the winner')
        return True
    if a[2][0] == a[2][1] and a[2][1] == a[2][2] and a[2][0] != '-':
        print(f'{a[2][0]} is the winner')
        return True
    if a[0][0] == a[1][0] and a[1][0] == a[2][0] and a[2][0] != '-':
        print(f'{a[0][0]} is the winner')
        return True
    if a[0][1] == a[1][1] and a[1][1] == a[2][1] and a[0][1] != '-':
        print(f'{a[0][1]} is the winner')
        return True
    if a[0][2] == a[1][2] and a[1][2] == a[2][2] and a[0][2] != '-':
        print(f'{a[0][2]} is the winner')
        return True
    else:    
        return False


def player_choice(a, player):
    while True:
        print_board(a)
        square = input(f'\nWhich square do you want to put {player} in\n\n')

        if square == 'top left':
            row = 0
            column =0
        elif square == 'top middle':
            row = 0
            column =1
        elif square == 'top right':
            row = 0
            column =2
        elif square == 'middle left':
            row = 1
            column =0
        elif square == 'middle':
            row = 1
            column =1
        elif square == 'middle right':
            row = 1
            column =2
        elif square == 'bottom left':
            row = 2
            column =0
        elif square == 'bottom middle':
            row = 2 
            column =1
        elif square == 'bottom right':
            row = 2
            column =2
        else:
            print ('Wrong choice')
            continue

        if a[row][column] == '-':
            break
        else:
            print(f'you can not choose {square} square because it is already chosen!')
    a[row][column] = player

def is_draw(a):
    empty_squares_count = 0
    for i in range(3):
        for j in range(3):
            if a[i][j] == '-':
                empty_squares_count = empty_squares_count + 1
    if empty_squares_count == 0:
        print('DRAW!, Nobody won the game')
        return True
    else:
        return False
        



a = [['-','-','-'],['-','-','-'],['-','-','-']]

for i in range (5):
    
    if is_winner(a):
        break
    if is_draw(a) == True:
        break
    
    player_choice(a, 'X')

    print_board(a)

    if is_winner(a):
        break
    if is_draw(a) == True:
        break


    player_choice(a ,'O')
    print_board(a)


