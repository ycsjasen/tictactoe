# building the board
# Board reset
def boardclear():
    global brd
    brd = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        6: ' ',
        5: ' ',
        7: ' ',
        8: ' ',
        9: ' ',
    }

#initializing brd variable
boardclear()

#board display
def brdprint():
    print('       |       |       ')
    print(f'   {brd[7]}   |   {brd[8]}   |   {brd[9]}   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print(f'   {brd[4]}   |   {brd[5]}   |   {brd[6]}   ')
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print(f'   {brd[1]}   |   {brd[2]}   |   {brd[3]}   ')
    print('       |       |       ')


# rematch prompt
def rematch():
    global gamestate
    inputcheck = True
    while inputcheck == True:
        gamestatevar = input('Would you like to play again? ').lower()
        if gamestatevar == 'y':
            gamestate = True
            inputcheck = False
        elif gamestatevar == 'n':
            gamestate = False
            inputcheck = False
        else:
            print('Please answer using Y or N')


# setting win conditions
def wincheck():
    global breaktest
    h1 = [brd[1], brd[2], brd[3]]
    h2 = [brd[4], brd[5], brd[6]]
    h3 = [brd[7], brd[8], brd[9]]
    v1 = [brd[1], brd[4], brd[7]]
    v2 = [brd[2], brd[5], brd[8]]
    v3 = [brd[3], brd[6], brd[9]]
    d1 = [brd[1], brd[5], brd[9]]
    d2 = [brd[7], brd[5], brd[3]]
    winlist = [h1, h2, h3, v1, v2, v3, d1, d2]
    if ['X', 'X', 'X'] in winlist:
        if rolechk == 1:
            print('Player One wins!')
        elif rolechk == 2:
            print('Player Two wins!')
        rematch()
        breaktest = 1
    elif ['O', 'O', 'O'] in winlist:
        if rolechk == 2:
            print('Player Two wins!')
        elif rolechk == 1:
            print('Player One wins!')
        rematch()
        breaktest = 1


# Starting the game; role assignment
gamestate = True
while gamestate == True:
    boardclear()
    #For tracking progress
    global i
    turncounter = 0
    inputtracker = list(range(1, 11))
    inputtracker.append('x')
    breaktest = 0
    rolechk = 0
    roles = {}
    xo = ('X', 'O')
    #determining roles
    while rolechk == 0:
        role = input('Hello Player One, would you like to be X or O? ').lower()
        if role == 'x':
            rolechk = 1
            roles['Player One'] = xo[0]
            roles['Player Two'] = xo[1]
        elif role == 'o':
            rolechk = 2
            roles['Player One'] = xo[1]
            roles['Player Two'] = xo[0]
        else:
            print('Please input either X or O to begin the game')

    print(f'Player One will be {roles["Player One"]}')
    print(f'Player Two will be {roles["Player Two"]}')
    brdprint()

    while turncounter < 9:

        if rolechk == 1:
            intcheck = False
            while intcheck == False:
                try:
                    i = int(input(f'Player One, please choose where you want to place your {roles["Player One"]}.  '))
                    intcheck = True
                except:
                    print('Please choose an empty spot number (1-9)')
            if i not in range(1, 10):
                print('Please choose an empty spot number (1-9)')
                continue
            elif i not in inputtracker:
                print('That spot is already taken!')
                continue
            elif i in inputtracker:
                iii = inputtracker.index(i)
                inputtracker.pop(iii)
            # populating the board with the corresponding mark
            brd[i] = roles['Player One']
            brdprint()
            wincheck()
            if breaktest == 1:
                break
            rolechk = 2
            turncounter += 1
        elif rolechk == 2:
            intcheck = False
            while intcheck == False:
                try:
                    i = int(input(f'Player Two, please choose where you want to place your {roles["Player Two"]}.  '))
                    intcheck = True
                except:
                    print('Please choose an empty spot number (1-9)')
            if i not in range(1, 10):
                print('Please choose an empty spot number (1-9)')
                continue
            elif i not in inputtracker:
                print('That spot is already taken!')
                continue
            elif i in inputtracker:
                iii = inputtracker.index(i)
                inputtracker.pop(iii)
            brd[i] = roles['Player Two']
            brdprint()
            wincheck()
            if breaktest == 1:
                break
            rolechk = 1
            turncounter += 1
    if turncounter == 9:
        print('Game Over, tie game.')
        rematch()
