class Node:
    def __init__(self, value):
        self.value = value


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


class Tree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


# left_child = Tree(3)
# right_child = Tree(4)
# parent = Tree(1, left_child, right_child)
# print(parent.right_child.data)

root_node = Tree(1, Tree(3), Tree(4))
print(root_node.data)


# ///////////////////////
