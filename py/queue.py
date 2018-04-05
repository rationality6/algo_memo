class Queue:
    def __init__(self):
        self.items = []

    def printing(self):
        return self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def reverse(self):
        self.items.reverse()

    def isEmpty(self):
        return self.items != []


def reverse_queue(string):
    result = ""
    queue = Queue()
    for i in string:
        queue.enqueue(i)
    queue.reverse()
    while queue.isEmpty():
        result += queue.dequeue()
    return result


queue0 = Queue()
queue0.enqueue(1)
queue0.enqueue(2)
queue0.enqueue(3)

print(reverse_queue("apple"))


class Queue:
    def __init__(self):
        self.items = []
