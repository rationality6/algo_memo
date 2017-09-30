# Equal Sides Of An Array

def find_even_index(arr):
    val0 = sum(arr)
    result = 0
    position = 0
    while position < len(arr):
        val0 -= arr[position]
        if result == val0:
            return position
        result += arr[position]
        position += 1
    return -1


def find_even_index(arr):
    for i in range(len(arr)):
        print(sum(arr[:i]),'foo')
        print(sum(arr[i + 1:]))
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


# print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3)
# print(find_even_index([1, 100, 50, -51, 1, 1]) == 1)
# print(find_even_index([1, 2, 3, 4, 5, 6]) == -1)
# print(find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3)
# print(find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0)
# print(find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6)
# print(find_even_index(range(1, 100)) == -1)
# print(find_even_index([0, 0, 0, 0, 0]) == 0)
# print(find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3)
# print(find_even_index(range(-100, -1)) == -1)
