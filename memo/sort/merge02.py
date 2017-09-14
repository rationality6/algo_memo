import random


class Sort_machine:
    def __init__(self, til):
        self.alist = [*range(til)]

    def random_arr(self):
        alist = self.alist
        for i in range(len(alist)):
            random_number = random.randint(0, len(alist) - 1)
            alist[i], alist[random_number] = alist[random_number], alist[i]

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        middle = int(len(lst) / 2)
        left = self.merge_sort(lst[:middle])
        right = self.merge_sort(lst[middle:])
        return self.merge(left, right)


sort0 = Sort_machine(100)
sort0.random_arr()
print(sort0.alist)

print(sort0.merge_sort(sort0.alist))
