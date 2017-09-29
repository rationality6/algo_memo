class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def init_tree():
    leaf = []
    for i in range(6):
        leaf.append(Node(i + 1))
    left_subsubtree = Node(7, leaf[0], leaf[1])
    right_subsubtree = Node(8, leaf[2], leaf[3])
    left_subtree = Node(9, left_subsubtree, right_subsubtree)
    right_subtree = Node(10, leaf[4], leaf[5])
    root = Node(11, left_subtree, right_subtree)
    return root


def preorder_traverse(tree):
    if tree == None:
        return tree
    preorder_traverse(tree.left_child)
    preorder_traverse(tree.right_child)
    print(tree.data)


root0 = init_tree()
preorder_traverse(root0)

# class Node:
#     def __init__(self, data, left_node=None, right_node=None):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node
#
#
#
# node = Node(0, Node(1), Node(2))
# node.left_node.left_node = Node(3)
# print(node.left_node.left_node.data)
