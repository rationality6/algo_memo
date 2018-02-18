def solution():
    for N in range(int(input())):
        data = input()
        oddChar = ""
        evenChar = ""
        for i, x in enumerate(list(data)):
            if i % 2 == 0:
                evenChar += x
            else:
                oddChar += x
        print(evenChar, oddChar)


char0 = "Hacker"
char1 = "Rank"

solution(char0)
solution(char1)

list0 = list(reversed(range(10)))


def bubble_sort(L):
    for i in reversed(range(len(L))):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j + 1], L[j] = L[j], L[j + 1]
    return L


print(bubble_sort(list0))


list0 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def selection_sort(L):
    for i in range(len(L)):
        index = i
        for j in range(i + 1, len(L)):
            if L[index] > L[j]:
                index = j
        L[index], L[i] = L[i], L[index]
    return L


print(selection_sort(list0))


list0 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def insertion_sort(L):
    for i in range(1, len(L)):
        current = L[i]
        index = i
        while index > 0 and current < L[index - 1]:
            L[index] = L[index - 1]
            index -= 1
        L[index] = current
    return L


print(insertion_sort(list0))


list0 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def merge(L, R):
    result = []
    l, r = 0, 0
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1
    result += L[l:]
    result += R[r:]
    return result


def merge_sort(L):
    if len(L) <= 1:
        return L
    middle = round(len(L) / 2)
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)


print(merge_sort(list0))
