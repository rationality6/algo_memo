reversed_list = [*reversed(range(10))]


def solver(L):
    for i in range(len(L)):
        index = i
        for j in range(i, len(L)):
            if L[index] > L[j]:
                index = j
        L[index], L[i], =  L[i], L[index]
    return L


print(reversed_list)
print(solver(reversed_list))

reversed_list = [*reversed(range(1,11))]
def bubble(L):
    length = len(L)
    for i in range(length -1 , -1, -1):
        print(i)
        for j in range(i):
            print(j)
            if L[j] > L[j+1]:
                L[j] ,L[j+1] = L[j+1], L[j]
    return L
print(reversed_list)
print(bubble(reversed_list))

reversed_list = [*reversed(range(1,11))]
def insertion(L):
    pass
