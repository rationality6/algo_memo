import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)
print(random_arr0)


def bubble_sort(arr):
    n = arr[:]
    for i in reversed(range(len(n))):
        for z in range(i):
            if n[z] > n[z + 1]:
                n[z], n[z + 1] = n[z + 1], n[z]
    return n


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i
        while 0 < pos and current < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = current


def selection_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length - 1):
        index = i
        for z in range(i + 1, arr_length):
            if arr[index] > arr[z]:
                index = z
        arr[index], arr[i] = arr[i], arr[index]


# print(bubble_sort(random_arr0))
# insertion_sort(random_arr0)
selection_sort(random_arr0)
print(random_arr0)
