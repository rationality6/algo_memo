class Tree:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def init_tree():
    leafs = []
    for i in range(6):
        leafs.append(Tree(i))
    left_subsubtree = Tree(6, leafs[0], leafs[1])
    right_subsubtree = Tree(7, leafs[2], leafs[3])
    left_subtree = Tree(8, left_subsubtree, right_subsubtree)
    right_subtree = Tree(9, leafs[4], leafs[5])
    root = Tree(10, left_subtree, right_subtree)
    return root


root0 = init_tree()


def preorder_traverse(tree):
    if tree == None:
        return
    print(tree.data)
    preorder_traverse(tree.left_child)
    preorder_traverse(tree.right_child)


def inorder_traverse(tree):
    if tree == None:
        return
    preorder_traverse(tree.left_child)
    print(tree.data)
    preorder_traverse(tree.right_child)


def postorder_traverse(tree):
    if tree == None:
        return
    preorder_traverse(tree.left_child)
    preorder_traverse(tree.right_child)
    print(tree.data)


preorder_traverse(root0)
# inorder_traverse(root0)
# postorder_traverse(root0)
