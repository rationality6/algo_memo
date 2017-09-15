import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)


def selection_sort(ARR):
    for i in range(len(ARR) - 1):
        index = i
        for z in range(i + 1, len(ARR)):
            if ARR[index] > ARR[z]:
                index = z
            ARR[index], ARR[i] = ARR[i], ARR[index]


random_arr0
selection_sort(random_arr0)
print(random_arr0)
