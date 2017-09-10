from random import randint


class Sort_machine():
    def random_arr(self, len):
        result = [*range(0, len)]
        for i in (range(len)):
            random_number = randint(0, len - 1)
            temp = result[i]
            result[i] = result[random_number]
            result[random_number] = temp
        return result

    def bubble_sort(self, ARR):
        for i in reversed(range(len(ARR))):
            for j in range(i):
                if ARR[j] > ARR[j + 1]:
                    temp = ARR[j]
                    ARR[j] = ARR[j + 1]
                    ARR[j + 1] = temp


ma0 = Sort_machine()
arr0 = ma0.random_arr(10)
print(arr0)
print(sorted(ma0.random_arr(10)) == [*range(10)])

arr1 = ma0.random_arr(10)
ma0.bubble_sort(arr1)
print(arr1)
