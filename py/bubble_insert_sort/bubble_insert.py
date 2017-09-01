from random import randint


class Sorting_machine:
    def __init__(self):
        self.arr = []

    def printing(self):
        print(self.arr)

    def make_array_suffle(self, til):
        self.arr = [i for i in range(til)]
        for i in range(0, len(self.arr)):
            random_number = randint(0, len(self.arr) - 1)
            temp = self.arr[i]
            self.arr[i] = self.arr[random_number]
            self.arr[random_number] = temp

    def make_random_array(self, start, end, til):
        for i in range(til):
            self.arr.append(randint(start, end))

    def swap(self, i):
        self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]

    def bubble_sort(self):
        for i in range(len(self.arr) - 1, 0, -1):
            for x in range(i):
                if self.arr[x] > self.arr[x + 1]:
                    self.swap(x)

    def insert_sort(self):
        for i in self.arr:
            print(i)

    def bubblesort_reverse(self):
        for i in range(len(self.arr)):
            for k in range(len(self.arr) - 1, i, -1):
                if (self.arr[k] < self.arr[k - 1]):
                    self.swap_reverse(k)

    def swap_reverse(self, i):
        self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]

    
