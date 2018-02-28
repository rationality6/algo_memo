class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def init_tree():
    arr = [4, 5, 6, 7]
    leafs = []
    for i in range(len(arr)):
        leafs.append(Node(arr[i]))
    left = Node(2, leafs[0], leafs[1])
    right = Node(3, leafs[2], leafs[3])
    root = Node(1, left, right)
    return root


root = init_tree()
print(root)


def preorder_traverse_in_interview(node):
    if node.data == 6:
        print(node.data)
    if node.left == None or node.right == None:
        return
    if node.data == 6:
        print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def preorder_traverse(node):
    if node.data == 6:
        print(node.data)
    if node.left == None or node.right == None:
        return
    # if node.data == 6:
    #     print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def inorder_traverse(node):
    if node == None:
        return
    if node.data == 6:
        print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def postorder_traverse(node):
    if node == None:
        return
    if node.data == 6:
        print(node.data)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


preorder_traverse(root)
# inorder_traverse(root)
# postorder_traverse(root)
