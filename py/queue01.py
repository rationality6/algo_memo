class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.insert(0, item)

    def dequeue(self):
        return self.arr.pop()

    def printing(self):
        print(self.arr)


queue00 = Queue()
queue00.enqueue(1)
queue00.enqueue(2)
queue00.enqueue(3)
queue00.printing()
print(queue00.dequeue())
print(queue00.dequeue())
queue00.printing()
print(queue00.dequeue())

# FIFO first in first out
