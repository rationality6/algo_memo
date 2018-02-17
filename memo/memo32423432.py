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

list0 = list(reversed(range(10)))
def selection_sort(L):
    for i in reversed(range(len(L))):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j + 1], L[j] = L[j], L[j + 1]
    return L
print(bubble_sort(list0))
