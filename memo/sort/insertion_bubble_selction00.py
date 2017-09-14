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
            current = alist[i]
            position = i
            while 0 < position and current < alist[position - 1]:
                alist[position] = alist[position - 1]
                position -= 1
            alist[position] = current

    def bubble_sort(self):
        alist = self.alist
        for i in reversed(range(len(alist))):
            for z in range(i):
                if alist[z] > alist[z + 1]:
                    alist[z + 1], alist[z] = alist[z], alist[z + 1]

    def selection_sort(self):
        alist = self.alist
        length = len(alist)
        for i in range(length - 1):
            index = i
            for z in range(i + 1, length):
                if alist[index] > alist[z]:
                    index = z
            alist[i], alist[index] = alist[index], alist[i]

    def merge_sort(self):
        print("hello")
        pass


sort0 = Sort_machine(10)
sort0.random_arr()
print(sort0.alist)

# sort0.bubble_sort()
# sort0.insertion_sort()
# sort0.selection_sort()
sort0.merge_sort()

print(sort0.alist)
