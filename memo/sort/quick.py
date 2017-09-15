import random


def random_arr(a, b):
    arr = [*range(a, b)]
    for i in range(len(arr)):
        random_number = random.randint(0, len(arr) - 1)
        arr[i], arr[random_number] = arr[random_number], arr[i]
    return arr


random_arr0 = random_arr(0, 10)
print(random_arr0)


def quicksort(list):
    if len(list) <= 1:
        return list

    less = []
    greater = []

    middle = int((len(list) - 1) / 2)
    pivot = list[middle]
    list.remove(pivot)
    for num in list:
        if num <= pivot:
            less.append(num)
        else:
            greater.append(num)
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(random_arr0))


def quicksort(x):
    if len(x) <= 1:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quicksort(alist))
