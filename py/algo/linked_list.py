class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insert_start(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    # O(1)
    def size1(self):
        return self.size

    # O(N)
    def size2(self):
        actual_node = self.head
        size = 0

        while actual_node is not None:
            size += 1
            actual_node = actual_node.next_node

        return size

    # O(N)
    def insert_end(self, data):

        self.size = self.size + 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    # O(N)
    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d " % actual_node.data)
            actual_node = actual_node.next_node


linked_list = LinkedList()

linked_list.insert_start(1)
linked_list.insert_start(2)
linked_list.insert_start(3)

linked_list.insert_end(321)

linked_list.traverse_list()
# print(linked_list.size1())
