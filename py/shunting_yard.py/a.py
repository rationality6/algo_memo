class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.insert(0, item)

    def dequeue(self):
        self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def printing(self):
        print(self.arr)


def changer(input):
    stack = []
    queue = []
    input_list = list(input)
    for i in range(0, input_list):
        print('foo')


queue0 = Queue()
queue0.enqueue(1)
queue0.enqueue(2)
queue0.enqueue(3)
queue0.printing()
print(queue0.peek())

changer("3+4")
