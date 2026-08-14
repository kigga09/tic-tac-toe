#----
real_moves = {
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': ''
}

diagonals = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '5', '9'], ['3', '5', '7'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]


#functions
moves = real_moves.keys()

def txt_init(txt):
    txt = txt.lower()
    txt = txt.replace(' ', '')
    txt = txt.replace('\n', '')
    txt = txt.replace('\t', '')
    txt = txt.replace('\r', '')


def isvalid(move):
    global real_moves
    if move in moves:
        if real_moves[move] == '':
            return True
        else:
            return False
    else:
        return False


def all_equal(list):
    ref = list[0]
    for item in list:
        if item != ref:
            return False
    return True


def show_table():
    print(f'''
{real_moves['1']} - {real_moves['2']} - {real_moves['3']}
{real_moves['4']} - {real_moves['5']} - {real_moves['6']}
{real_moves['7']} - {real_moves['8']} - {real_moves['9']}
''')


def player_turn(x_o):
    global turn, move, moves, real_moves, running
    #move = txt_init(move)
    if move == 'q':
        running = False
    elif move in moves:
        for i in moves:
            if move == i:
                if isvalid(i):
                    real_moves[i] = x_o
                else:
                    print('invalid move')
    else:
        print('invalid move')


#game loop

choice = None
turn = None #true--> players turn ; false--> computers turn
running = True
while running:
    if choice is None:
        choice = input('''chose who to make the 1st move
        0. you
        1. computer
        q. quite 
            (type 'q' whenever u wanna quit)
        > ''')
        #choice = txt.init(choice)
        if choice == 'q':
            break
        elif choice == '1':
            turn = True
            x_o = 'X'
        elif choice == '0':
            turn = False
            x_o = 'O'
        else:
            print('invalid input')
            continue

    if turn:
        print('='*20)
        show_table()
        move = input('whats ur move > ')
        player_turn(x_o)
        turn = False
    else:
        print('='*20, '\ncomputer played the mbappe special')
        turn = True
