import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)


def bubble_sort(L):
    for i in reversed(range(len(L))):
        for z in range(i):
            if L[z] > L[z + 1]:
                L[z], L[z + 1] = L[z + 1], L[z]


print(random_arr0)
bubble_sort(random_arr0)
print(random_arr0)
