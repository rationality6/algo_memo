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
