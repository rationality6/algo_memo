class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def init_tree():
    arr0 = ['D', 'E', 'F', 'G']
    leafs = []
    for i in range(len(arr0)):
        leafs.append(Node(arr0[i]))
    left1 = Node('B', leafs[0], leafs[1])
    right1 = Node('C', leafs[2], leafs[3])
    root = Node('A', left1, right1)
    return root


root0 = init_tree()


def preorder_traverse(tree):
    if tree == None:
        return
    print(tree.data)
    preorder_traverse(tree.left)
    preorder_traverse(tree.right)


def inorder_traverse(tree):
    if tree == None:
        return
    preorder_traverse(tree.left)
    print(tree.data)
    preorder_traverse(tree.right)


def postorder_traverse(tree):
    if tree == None:
        return
    preorder_traverse(tree.left)
    preorder_traverse(tree.right)
    print(tree.data)


def invert(root):
    if root is None:
        return
    inverted = Node(root.data)
    inverted.left = invert(root.right)
    inverted.right = invert(root.left)
    return inverted


levelq = []


def levelorder_traverse(tree):
    global levelq
    levelq.append(tree)
    while len(levelq) != 0:
        visit_node = levelq.pop(0)
        print(visit_node.data)
        if visit_node.left != None:
            levelq.append(visit_node.left)
        if visit_node.right != None:
            levelq.append(visit_node.right)


# preorder_traverse(root0)
# inorder_traverse(root0)
# postorder_traverse(root0)
# levelorder_traverse(root0)
inverted_root = invert(root0)
levelorder_traverse(inverted_root)


print(True == True)
