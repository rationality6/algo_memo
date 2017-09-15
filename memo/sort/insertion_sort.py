import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)

def insertion_sort(ARR):
    for i in range(len(ARR)):
        current = ARR[i]
        index = i
        while index > 0 and current < ARR[index - 1]:
            ARR[index] = ARR[index - 1]
            index -= 1
        ARR[index] = current



insertion_sort(random_arr0)
print(random_arr0)
