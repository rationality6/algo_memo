import os


def print_current_state(alist, icons, turn):
    print('{} | {} | {}'.format(alist[0], alist[1], alist[2]))
    print('{} | {} | {}'.format(alist[3], alist[4], alist[5]))
    print('{} | {} | {}'.format(alist[6], alist[7], alist[8]))
    print('turn', icons[turn])


def turn_countor(turn_data):
    turn_data += 1
    return turn_data % 2


def result_condition_line(L, one, two, three):
    return L[one] == L[two] and L[two] == L[three]


def result_condition(check_func, L):
    if check_func(L, 0, 1, 2):
        return True
    if check_func(L, 3, 4, 5):
        return True
    if check_func(L, 6, 7, 8):
        return True
    if check_func(L, 0, 3, 6):
        return True
    if check_func(L, 1, 4, 7):
        return True
    if check_func(L, 2, 5, 8):
        return True
    if check_func(L, 0, 4, 8):
        return True
    if check_func(L, 2, 4, 6):
        return True


def tic_tac_toe_game():
    os.system('clear')
    game_list = [*range(1, 10)]
    icons = ["O", "X"]
    turn = 0
    turn_total_count = 0
    user_choose = False

    while True:

        if user_choose:
            if user_choose.isdecimal():
                user_choose = int(user_choose)
                if 0 < user_choose and user_choose < 10:
                    user_choose -= 1
                    if game_list[user_choose] in icons:
                        print("already choosed")
                    else:
                        game_list[user_choose] = icons[turn]
                        turn = turn_countor(turn)
                        turn_total_count += 1
                else:
                    print("Choose a number between 1~9")
            else:
                print("Type a numbers")

        print_current_state(game_list, icons, turn)

        print(turn_total_count, 'turn_total_count')
        a = result_condition(result_condition_line, game_list)
        b = turn_total_count >= 9
        if a or b:
            break

        user_choose = input("Select a spot: ")
        os.system('clear')

    print('win', icons[turn_countor(turn)])

tic_tac_toe_game()
