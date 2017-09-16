class Node:
    def __init___(self, data, leftNode=None, rightNode=None):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode

    def isLeaf(self):
        retur not self.left

    def isLeaf(self):
        return not self.leftNode and not self.rightNode

    def hasLeft(self):
        return not (self.leftNode is None)

    def hasRight(self):
        return not (self.rightNode is None)


class BinarySearchTree:
    def __init__(self root=None):
        self.root = root
        self.size = 0
        if root:
            self.size = 1

    def search(self, key):
        temp = self.root
        while temp:
            if temp.key == key
                return self.root
            if temp.key > key:
                temp = temp.leftNode
            else:
                temp = temp.rightNode
        return None
