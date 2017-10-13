def rpc_game():
    import random
    number_of_cases = [0, 1, 2]
    user_choice = random.choice(number_of_cases)
    computer_choice = random.choice(number_of_cases)
    if user_choice == computer_choice:
        return user_choice, computer_choice, "Draw"
    else:
        if user_choice == 0:
            if computer_choice == 1:
                return user_choice, computer_choice, "User Win"
            else:
                return user_choice, computer_choice, "Computer Win"
        elif user_choice == 1:
            if computer_choice == 2:
                return user_choice, computer_choice, "User Win"
            else:
                return user_choice, computer_choice, "Computer Win"
        else:
            if computer_choice == 1:
                return user_choice, computer_choice, "Computer Win"
            else:
                return user_choice, computer_choice, "User Win"


def rpc_game_test(func, n):
    result = True
    for i in range(n):
        a, b, func_result = func()
        if a == b:
            if func_result != "Draw":
                result = False
                print("here!")
        else:
            if a == 0:
                if b == 1:
                    if func_result != "User Win":
                        result = False
                else:
                    if func_result != "Computer Win":
                        result = False
            elif a == 1:
                if b == 2:
                    if func_result != "User Win":
                        result = False
                else:
                    if func_result != "Computer Win":
                        result = False
            else:
                if b == 1:
                    if func_result != "Computer Win":
                        result = False
                else:
                    if func_result != "User Win":
                        result = False
                        print(a, b, func_result)
    return result


print(rpc_game_test(rpc_game, 100000))
