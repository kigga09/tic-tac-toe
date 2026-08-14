import random as rn

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

diagonals = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['1', '5', '9'],
            ['3', '5', '7'],
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9']
            ]

moves = real_moves.keys()

def result():
    for i in diagonals:
        if all_equal([real_moves[j] for j in i]) and real_moves[i[0]] != '':
            return 'win'

    if all(real_moves[i] != '' for i in moves):
        return 'draw'

    return None

def txt_init(txt):
    txt = txt.lower()
    txt = txt.replace(' ', '')
    txt = txt.replace('\n', '')
    txt = txt.replace('\t', '')
    txt = txt.replace('\r', '')
    return txt

def isvalid(move):
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
{real_moves['1'] or '1'} - {real_moves['2'] or '2'} - {real_moves['3'] or '3'}
{real_moves['4'] or '4'} - {real_moves['5'] or '5'} - {real_moves['6'] or '6'}
{real_moves['7'] or '7'} - {real_moves['8'] or '8'} - {real_moves['9'] or '9'}
''')

def player_turn(x_o):
    global move, running

    move = txt_init(move)

    if move == 'q':
        running = False
        return False

    elif isvalid(move):
        real_moves[move] = x_o
        return True

    else:
        print('invalid move')
        return False


choice = None
turn = None
running = True

while running:

    if choice is None:
        choice = input('''chose who to make the 1st move
        0. you
        1. computer
        q. quite
            (type 'q' whenever u wanna quit)
        > ''')

        choice = txt_init(choice)

        if choice == 'q':
            break

        elif choice == '0':
            turn = True
            player_x_o = 'X'
            computer_x_o = 'O'

        elif choice == '1':
            turn = False
            player_x_o = 'O'
            computer_x_o = 'X'

        else:
            print('invalid input')
            choice = None
            continue

    if turn:
        print('=' * 20)
        show_table()

        move = input('whats ur move > ')

        if player_turn(player_x_o):
            if result() == 'win':
                show_table()
                print('you win!')
                break

            elif result() == 'draw':
                show_table()
                print('draw!')
                break

            turn = False

    else:
        print('=' * 20)

        available = [i for i in moves if real_moves[i] == '']
        move = rn.choice(available)

        real_moves[move] = computer_x_o

        print('computer played:', move)

        if result() == 'win':
            show_table()
            print('computer wins!')
            break

        elif result() == 'draw':
            show_table()
            print('draw!')
            break

        turn = True