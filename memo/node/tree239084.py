class Tree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


# left_child = Tree(2)
# right_child = Tree(3)
# parent = Tree(1, left_child, right_child)
# print(parent.right_child.data)

# root = Tree(1, Tree(2), Tree(3))
# print(root.right_child.data)


def init_tree():
    leaf = []
    for i in range(6):
        leaf.append(Tree(i + 1))

    left_subsubtree = Tree(7, leaf[0], leaf[1])
    right_subsubtree = Tree(8, leaf[2], leaf[3])
    left_subtree = Tree(9, left_subsubtree, right_subsubtree)
    right_subtree = Tree(10, leaf[4], leaf[5])
    root = Tree(11, left_subtree, right_subtree)
    return root


root0 = init_tree()


def preorder_traverse(tree):
    if tree == None:
        return
    preorder_traverse(tree.left_child)
    print(tree.data)
    preorder_traverse(tree.right_child)


preorder_traverse(root0)
