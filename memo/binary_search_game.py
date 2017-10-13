import random


def init(start, end):
    arr = [*range(start, end)]
    answer_number = random.randint(start, len(arr))
    return arr, answer_number


def linear_search(start, end):
    arr, ans = init(start, end)
    count = 0
    for i in range(start, len(arr)):
        count += 1
        if arr[i] == ans:
            return count
    return -1


def binary_search(arr, anwser):
    found = False
    top = len(arr) - 1
    bottom = 0
    count = 0
    while bottom <= top and not found:
        guess = (top + bottom) // 2
        count += 1
        if anwser == arr[guess]:
            found = True
        elif anwser > arr[guess]:
            bottom = guess + 1
        else:
            top = guess - 1
    return count


def binary_search_recur(array, value, low=0, high=0):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] > value:
        return binary_search_recur(array, value, low, mid - 1)
    elif array[mid] < value:
        return binary_search_recur(array, value, mid + 1, high)
    else:
        return mid


# print(sum(binary_search([*range(0, 100)], random.randint(0, 100)) for i in range(100)) / 100)


def average(func, start, end, try_n):
    return sum(func(start, end) for i in range(try_n)) / try_n


# print(average(linear_search, 0, 100, 100))
print(binary_search_recur([*range(0, 100)], random.randint(0, 100), 0, 100))
# print(average(binary_search, 0, 100, 100))
