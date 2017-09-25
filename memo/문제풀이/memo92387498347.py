import random


def foobar(N):
    arr = [*range(0, N)]
    for i in range(0,5):
        random_number = random.randint(0, N - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


print(foobar(10))
