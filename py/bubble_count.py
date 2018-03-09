def bubble_sort(L):
    numberOfSwaps = 0
    for i in range(len(L) - 1, -1, -1):
        for j in range(0, i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                numberOfSwaps += 1
    return [L, numberOfSwaps]


list0 = [5, 4, 3, 2, 1]

result = bubble_sort(list0)
result_sorted = result[0]
result_count = result[1]

print("Array is sorted in {} swaps.".format(result_count))
print("First Element: {}".format(result_sorted[0]))
print("Last Element: {}".format(result_sorted[-1]))
