value = 0


def recur():
    global value
    if value < 50:
        value += 1
        recur()
        print(value)


recur()
