class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y


class Math2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


class Math3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m1 = Math(x, y)
        self.m2 = Math2(x, y)

    def power(self):
        return self.x ** self.y

    def add(self):
        return self.m1.add()

    def subtract(self):
        return self.m1.subtract()

    def multiply(self):
        return self.m2.multiply()


m0 = Math3(8, 3)
print(m0.add())
print(m0.subtract())
print(m0.)
