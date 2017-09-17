class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, i):
        self.arr.insert(0, i)

    def dequeue(self):
        return self.arr.pop()

    def printing(self):
        print(self.arr)


q = Queue()
print(q.arr)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.arr)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
