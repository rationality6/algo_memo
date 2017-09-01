class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def printing(self):
        return self.items

    def peekLast(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def push(self, payload):
        self.items.append(payload)

    def pop(self):
        return self.items.pop()


def reverse_string(input):
    stack0 = Stack()
    result = ""
    for i in input:
        stack0.push(i)
    while stack0.isEmpty() != True:
        result += stack0.pop()
    return result


print(reverse_string("apple"))
