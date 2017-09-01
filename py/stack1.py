class Stack():
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def isEmpty(self):
        return self.array != []

    def printing(self):
        print(self.array)


stack0 = Stack()
stack0.push(1)
stack0.push(2)
stack0.push(3)
stack0.printing()
print(stack0.pop())
stack0.printing()


def reverse_string(input):
    result = ""
    stack = Stack()
    for i in input:
        stack.push(i)
    while stack.isEmpty():
        result += stack.pop()
    return result


print(reverse_string("apple"))
