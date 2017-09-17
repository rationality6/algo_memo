class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_in_tree(root, value):
    new_node = Node(value)
    current = root
    while True:
        if value <= current.value:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
    return root


def array_to_tree(values):
    root = Node(values[0])

    for value in values[1:]:
        root = insert_in_tree(root, value)

    return root


def invert(root):
    if root is None:
        return None

    inverted = Node(root.value)

    inverted.left = invert(root.right)
    inverted.right = invert(root.left)
    return inverted


def preorder(root):
    if root is None:
        return []

    # current, left, right
    return [root.value] + preorder(root.left) + preorder(root.right)


def solve():
    whitelist = re.compile('^\[[0-9, ]*]$')

    receive()

    while True:
        level = receive()
        array = level.split(": ")[1]
        if whitelist.match(array):
            # anti-rootkit v2
            array = eval(array)
        else:
            quit()
        print "GOT ARRAY: ", array

        tree = array_to_tree(array)
        send(preorder(invert(tree)))
