class Tree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def init_tree():
    leaf = []
    for i in range(6):
        leaf.append(Tree(i + 1))
    print(leaf)

    left_subtree = Tree(
        9, Tree(7, leaf[0], leaf[1]), Tree(8, leaf[2], leaf[3]))
    right_subtree = Tree(10, leaf[4], leaf[5])

    root = Tree(11, left_subtree, right_subtree)
    return root


root = init_tree()
print(root.data)
