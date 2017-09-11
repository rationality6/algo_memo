class Node:
    # my first tree class
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def invert(root):
        if root is None:
            return None

        inverted = Node(root.value)

        inverted.left = invert(root.right)
        inverted.right = invert(root.left)
        return inverted

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def invert(root):
        if root is None:
            return None:
        inverted = Node(root.value)
        inverted.left = inver
