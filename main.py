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


# ----------

def result():
    for i in diagonals:
        if all_equal([real_moves[j] for j in i]) and real_moves[i[0]] != '':
            return real_moves[i[0]]

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


def available_moves():
    return [i for i in moves if real_moves[i] == '']


# ---------- MINIMAX ----------

def minmax():
    # If the computer has already won
    if result() == computer_x_o:
        return 1

    # If the player has already won
    elif result() == player_x_o:
        return -1

    # If the game is a draw
    elif result() == 'draw':
        return 0

    # Computer tries to get the highest score
    best_score = -100

    for move in available_moves():

        # Computer temporarily plays this move
        real_moves[move] = computer_x_o

        # Now let the opponent play
        score = min_player()

        # Undo the move
        real_moves[move] = ''

        if score > best_score:
            best_score = score

    return best_score


def min_player():
    # If the computer has won
    if result() == computer_x_o:
        return 1

    # If the player has won
    elif result() == player_x_o:
        return -1

    # If draw
    elif result() == 'draw':
        return 0

    # Player tries to get the lowest score
    best_score = 100

    for move in available_moves():

        # Player temporarily plays this move
        real_moves[move] = player_x_o

        # Now let the computer play
        score = min_computer()

        # Undo the move
        real_moves[move] = ''

        if score < best_score:
            best_score = score

    return best_score


def min_computer():
    # If the computer has won
    if result() == computer_x_o:
        return 1

    # If the player has won
    elif result() == player_x_o:
        return -1

    # If draw
    elif result() == 'draw':
        return 0

    best_score = -100

    for move in available_moves():

        real_moves[move] = computer_x_o

        score = min_player()

        real_moves[move] = ''

        if score > best_score:
            best_score = score

    return best_score


def best_move():
    best_score = -100
    best_move = None

    for move in available_moves():

        # Try the move
        real_moves[move] = computer_x_o

        # See how good this move eventually becomes
        score = min_player()

        # Undo the move
        real_moves[move] = ''

        # Keep the best move
        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def var_reset():
    global choice, turn, difficulty, running

    choice = None
    turn = None
    difficulty = None

    for i in moves:
        real_moves[i] = ''

def play_again():
    while True:
        again = input('do u wanna play again? (y/n) > ')
        again = txt_init(again)

        if again == 'y':
            var_reset()
            return True

        elif again == 'n':
            print('quitting...')
            running = False
            return False

        else:
            print('invalid input')

# ---------

choice = None
turn = None
difficulty = None
running = True

while running:

    if choice is None:
        print('=' * 20)
        choice = input('''\nchose who to make the 1st move
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
#difficulty selection
    if difficulty is None:
        print('=' * 20)
        difficulty = input('''chose difficulty
        0. easy
        1. hard
        > ''')

        difficulty = txt_init(difficulty)
        if difficulty not in ['0', '1']:
            print('invalid input')
            difficulty = None
            continue

    #player turn

    if turn:
        print('=' * 20)
        show_table()

        move = input('whats ur move > ')

        if player_turn(player_x_o):

            if result() == player_x_o:
                show_table()
                print('you win!')
                if play_again():
                    continue
                else:
                    break

            elif result() == 'draw':
                show_table()
                print('draw!')
                if play_again():
                    continue
                else:
                    break

            turn = False

    # computer turn

    else:
            
        print('=' * 20)
        if difficulty == '0':
            move = rn.choice(available_moves())
        elif difficulty == '1':
            move = best_move()

        real_moves[move] = computer_x_o

        print('computer played:', move)

        if result() == computer_x_o:
            show_table()
            print('computer wins!')
            if play_again():
                continue
            else:
                break

        elif result() == 'draw':
            show_table()
            print('draw!')
            if play_again():
                continue
            else:
                break

        turn = True