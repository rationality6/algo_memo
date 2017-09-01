class Multi_table:
    def __init__(self):
        self.arr = []

    def loop_stack(self, x, y):
        for x in range(x + 1):
            for y in range(y + 1):
                self.arr.append("{} * {} = {}".format(x, y, x * y))

    def printing(self):
        return self.arr


table0 = Multi_table()
table0.loop_stack(9, 9)
print(table0.printing())
