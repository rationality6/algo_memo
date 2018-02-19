import random


def search(LIST, ITEM):
    position = 0
    found = False
    while position < len(LIST) and not found:
        if LIST[position] == ITEM:
            found = True
        position += 1
    return found


def binary_search(LIST, ITEM):
    found = False
    top = len(LIST) - 1
    bottom = 0
    while bottom <= top and not found:
        middle = (bottom + top) // 2
        if LIST[middle] == ITEM:
            found = True
        elif ITEM > LIST[middle]:
            bottom = middle + 1
        else:
            top = middle - 1
    return found


def binary_search(array, value, low=0, high=0):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] > value:
        return binary_search(array, value, low, mid - 1)
    elif array[mid] < value:
        return binary_search(array, value, mid + 1, high)
    else:
        return mid


def random_arr(a, b):
    arr0 = [*range(a, b)]
    for i in range(len(arr0)):
        rn = random.randint(0, len(arr0) - 1)
        arr0[i], arr0[rn] = arr0[rn], arr0[i]
    return arr0


arr0 = random_arr(0, 10)
# print(search(arr0, 10))
print(binary_search([*range(0, 100)],random.randint(0,100) , 0, 100))
