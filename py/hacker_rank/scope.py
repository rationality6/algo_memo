def solution(L):
    return abs(max(L) - min(L))


list0 = [1, 2, 5]

class Difference:
    def __init__(self, a):
        self.__elements = a


d = Difference(list0)
print(d.__elements)
