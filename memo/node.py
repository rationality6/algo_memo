class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data)
            current = current.next

    def insert(self, head, data):
        if head == None:
            head == Node(data)
        else:
            self.inset(head.next,data)


sample = [2, 3, 4, 1]
mylist = Solution()
T = len(sample)
head = None
for i in range(T):
    data = sample[i]
    head = mylist.insert(head, data)
mylist.display(head)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
