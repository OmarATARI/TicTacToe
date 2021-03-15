global tab, select_box, select_symbol, list_nb, select_box_ia, select_symbol_ia
global my_score, ia_score
import random
list_nb = [x for x in range(0,9)]
my_score = ia_score = 0

tab = []

def reinitialize_game():
    global tab, list_nb
    tab = []
    list_nb = [x for x in range(0,9)]
    for i in range(1,4):
        tab.append([['  '],['  '],['  ']])

def display_playground():
    for v in zip(*tab):
        print(*v)

reinitialize_game()

def ask_position():
    global select_box
    while True:
        try:
            select_box = int(input(f'Saisir le numéro de la case à jouer ({", ".join(list(map(str,list_nb)))}): '))
            if int(select_box) in list_nb:
                break
        except ValueError:
            print("Ce n'est pas un nombre.")
def ask_symbol():
    global select_symbol
    while True:
        select_symbol = input ("Voulez vous jouer croix ou rond[X/O]? : ")
        if select_symbol.upper() in ['X', 'O']:
            if select_symbol.upper() == 'X':
                select_symbol = '❌'
            elif select_symbol.upper() == 'O':
                select_symbol = '⚫'
            break

def reverse_symbol(player_symbol):
    if player_symbol == '⚫':
        return '❌'
    elif player_symbol == '❌':
        return '⚫'

def ask_user():
    global select_symbol
    try:
        if select_symbol:
            pass
    except NameError:
        ask_symbol()
    ask_position()

def play_round():
    ask_user()
    apply_real_position_player()

def auto_play_round(sel_box, s_symbol):
    box_to_play = check_if_winnable(s_symbol)
    if not box_to_play:
        box_to_play = check_prevent_from_lost()
    if not box_to_play:
        apply_real_position_ia(sel_box, s_symbol)

def check_prevent_from_lost():
    global select_symbol
    return check_if_winnable(select_symbol, True)

def check_if_winnable(ia_symbol, is_to_defend = False):
    global tab, list_nb
    for t in tab:
        for i in range(0,3):
            # rows completion conditions
            cdrw1 = (tab[i][0] == tab[i][1] == [ia_symbol] and tab[i][2][0] == '  ')
            cdrw2 = (tab[i][0] == tab[i][2] == [ia_symbol] and tab[i][1][0] == '  ')
            cdrw3 = (tab[i][2] == tab[i][1] == [ia_symbol] and tab[i][0][0] == '  ')

            # col completion conditions
            cdcw1 = (tab[0][i] == tab[1][i] == [ia_symbol] and tab[2][i][0] == '  ')
            cdcw2 = (tab[0][i] == tab[2][i] == [ia_symbol] and tab[1][i][0] == '  ')
            cdcw3 = (tab[2][i] == tab[1][i] == [ia_symbol] and tab[0][i][0] == '  ')

            # left diag completion conditions
            dgl1 = (tab[0][0] == tab[2][2] == [ia_symbol] and tab[1][1][0] == '  ')
            dgl2 = (tab[0][0] == tab[1][1] == [ia_symbol] and tab[2][2][0] == '  ')
            dgl3 = (tab[1][1] == tab[2][2] == [ia_symbol] and tab[0][0][0] == '  ')

            # right diag completion conditions
            dgr1 = (tab[2][0] == tab[1][1] == [ia_symbol] and tab[0][2][0] == '  ')
            dgr2 = (tab[2][0] == tab[0][2] == [ia_symbol] and tab[1][1][0] == '  ')
            dgr3 = (tab[0][2] == tab[1][1] == [ia_symbol] and tab[2][0][0] == '  ')

            if cdrw1:
                if not is_to_defend:
                    tab[i][2] = [ia_symbol]
                    if i*3+2 in list_nb:
                        list_nb.remove(i*3+2)
                else:
                    tab[i][2] = [reverse_symbol(ia_symbol)]
                    if i*3+2 in list_nb:
                        list_nb.remove(i*3+2)
                return tab[i][2]
            elif cdrw2:
                if not is_to_defend:
                    tab[i][1] = [ia_symbol]
                    if i*3+1 in list_nb:
                        list_nb.remove(i*3+1)
                else:
                    tab[i][1] = [reverse_symbol(ia_symbol)]
                    if i*3+1 in list_nb:
                        list_nb.remove(i*3+1)
                return tab[i][1]
            elif cdrw3:
                if not is_to_defend:
                    tab[i][0] = [ia_symbol]
                    if i*3 in list_nb:
                        list_nb.remove(i*3)
                else:
                    tab[i][0] = [reverse_symbol(ia_symbol)]
                    if i*3 in list_nb:
                        list_nb.remove(i*3)
                return tab[i][0]

            if cdcw1:
                if not is_to_defend:
                    tab[2][i] = [ia_symbol]
                    if 6+i in list_nb:
                        list_nb.remove(6+i)
                else:
                    tab[2][i] = [reverse_symbol(ia_symbol)]
                    if 6+i in list_nb:
                        list_nb.remove(6+i)
                return tab[2][i]
            elif cdcw2:
                if not is_to_defend:
                    tab[1][i] = [ia_symbol]
                    if 3+i in list_nb:
                        list_nb.remove(3+i)
                else:
                    tab[1][i] = [reverse_symbol(ia_symbol)]
                    if 3+i in list_nb:
                        list_nb.remove(3+i)
                return tab[1][i]
            elif cdcw3:
                if not is_to_defend:
                    tab[0][i] = [ia_symbol]
                    if i in list_nb:
                        list_nb.remove(i)
                else:
                    tab[0][i] = [reverse_symbol(ia_symbol)]
                    if i in list_nb:
                        list_nb.remove(i)
                return tab[0][i]

            if dgl1:
                if not is_to_defend:
                    tab[1][1] = [ia_symbol]
                    if 4 in list_nb:
                        list_nb.remove(4)
                else:
                    tab[1][1] = [reverse_symbol(ia_symbol)]
                    if 4 in list_nb:
                        list_nb.remove(4)
                return tab[1][1]
            elif dgl2:
                if not is_to_defend:
                    tab[2][2] = [ia_symbol]
                    if 8 in list_nb:
                        list_nb.remove(8)
                else:
                    tab[2][2] = [reverse_symbol(ia_symbol)]
                    if 8 in list_nb:
                        list_nb.remove(8)
                return tab[2][2]
            elif dgl3:
                if not is_to_defend:
                    tab[0][0] = [ia_symbol]
                    if 0 in list_nb:
                        list_nb.remove(0)
                else:
                    tab[0][0] = [reverse_symbol(ia_symbol)]
                    if 0 in list_nb:
                        list_nb.remove(0)
                return tab[0][0]

            if dgr1:
                if not is_to_defend:
                    tab[0][2] = [ia_symbol]
                    if 2 in list_nb:
                        list_nb.remove(2)
                else:
                    tab[0][2] = [reverse_symbol(ia_symbol)]
                    if 2 in list_nb:
                        list_nb.remove(2)
                return tab[0][2]
            elif dgr2:
                if not is_to_defend:
                    tab[1][1] = [ia_symbol]
                    if 4 in list_nb:
                        list_nb.remove(4)
                else:
                    tab[1][1] = [reverse_symbol(ia_symbol)]
                    if 4 in list_nb:
                        list_nb.remove(4)
                return tab[1][1]
            elif dgr3:
                if not is_to_defend:
                    tab[2][0] = [ia_symbol]
                    if 6 in list_nb:
                        list_nb.remove(6)
                else:
                    tab[2][0] = [reverse_symbol(ia_symbol)]
                    if 6 in list_nb:
                        list_nb.remove(6)
                return tab[2][0]
        return False


def update_score(iswon):
    global my_score, ia_score
    if iswon:
        my_score += 1
    else:
        ia_score += 1
    print(f'Vous avez {my_score} point(s). L\'ordniateur a {ia_score} point(s)')

def start_the_game():
    while True:
        if not list_nb:
            break
        play_round()
        if check_winner() == '❌' or check_winner() == '⚫':
            print(f'Vous avez gagnée !')
            update_score(True)
            break
        try:
            auto_play_round(random.choice(list_nb), reverse_symbol(select_symbol))
        except IndexError:
            pass
        if check_winner() == '❌' or check_winner() == '⚫':
            print(f'Vous avez perdu !')
            update_score(False)
            break
        if not list_nb:
            break
        display_playground()
    display_playground()
    restart = input('Nouvelle partie ? [Y/N]')
    if restart.upper() == 'Y':
        reinitialize_game()
        display_playground()
        start_the_game()

def check_winner():
    for condition in check_conditions():
        if condition != False:
            return condition[0]

def check_conditions():
    conditions = []
    for t in tab:
        for i in range(0,3):
            conditions.append(check_win_condition(tab[i][0], tab[i][1], tab[i][2]))
            conditions.append(check_win_condition(tab[0][i], tab[1][i], tab[2][i]))
        conditions.append(check_win_condition(tab[0][0], tab[1][1], tab[2][2]))
        conditions.append(check_win_condition(tab[2][0], tab[1][1], tab[0][2]))
    return conditions

def check_win_condition(v1, v2, v3):
    if v1 == v2 == v3 != ['  ']:
        return v1
    else:
        return False

def apply_real_position_player():
    global select_box, select_symbol, select_box_ia, select_symbol_ia
    apply_real_position(select_box, select_symbol)


def apply_real_position_ia(s_box, s_symbol):
    global select_box_ia, select_symbol_ia
    if s_box and s_symbol:
        select_box_ia = s_box
        select_symbol_ia = s_symbol
    apply_real_position(select_box_ia, select_symbol_ia)


def apply_real_position(s_box, s_symbol):
    if type(s_box) != int:
        s_box = [s_symbol]
    else:
        for item in tab:
            if s_box > -1 and s_box < 3:
                tab[0][s_box] = [s_symbol]
            elif s_box > 2 and s_box < 6:
                tab[1][s_box%3] = [s_symbol]
            elif s_box > 5  and s_box < 9:
                tab[2][s_box%3] = [s_symbol]
            if s_box in list_nb:
                list_nb.remove(s_box)

start_the_game()
