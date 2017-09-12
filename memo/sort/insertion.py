import random


class Sort_machine:
    def __init__(self, til):
        self.alist = [*range(til)]

    def random_arr(self):
        alist = self.alist
        for i in range(len(alist)):
            random_number = random.randint(0, len(alist) - 1)
            alist[i], alist[random_number] = alist[random_number], alist[i]

    def foobar(self):
        print("foobar")

    def insertion_sort(self):
        alist = self.alist
        for i in range(1, len(alist)):
            pos = i
            cur = alist[i]
            while pos > 0 and cur < alist[pos - 1]:
                alist[pos] = alist[pos - 1]
                pos -= 1
            alist[pos] = cur

    def bubble_sort(self):
        alist = self.alist
        for i in reversed(range(len(alist))):
            for z in range(i):
                if alist[z] > alist[z + 1]:
                    alist[z], alist[z + 1] = alist[z + 1], alist[z]


sort0 = Sort_machine(20)
sort0.random_arr()
print(sort0.alist)
# sort0.bubble_sort()
sort0.insertion_sort()
print(sort0.alist)
