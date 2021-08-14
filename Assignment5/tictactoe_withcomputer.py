import random

game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

def show_game():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')  
        print() 
    print()
    
def enter_rc():   
    while True:
        row = int(input('row: '))
        if 0 <= row <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue 
        column = int(input('column: '))
        if 0 <= row <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue
        
        if game[row - 1][column - 1] == '_':     
            game[row - 1][column - 1] = 'X'
            break
        else:
            print('WARNING! Repetitive selection, Try Again ...')

def enter_rc_computer():
    while True:
        r = random.randint(1, 3)
        c = random.randint(1, 3)
        
        if game[r - 1][c - 1] == '_':
            game[r - 1][c - 1] = 'O'
            break

def end_game():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            return 1
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            return 2 
        
    for i in range(3):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            return 1
        if game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            return 2 
    
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        return 1
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        return 2
        
    return 0
      
flag = 0        
for i in range(9):
    if i % 2 == 0:
        enter_rc()
    elif i % 2 != 0:
        enter_rc_computer()
    
    show_game()
    
    e = end_game()
    if e != 0:
        flag = 1
        print('End Game')
        if e == 1:
            print('Player is Winner :)')
        if e == 2:
            print('Computer is winner :(')
        break

if flag == 0:
    print('End Game')
    print('DRAW :|')