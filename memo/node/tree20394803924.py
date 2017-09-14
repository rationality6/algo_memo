class BinaryTree:
    class Node:
        def __init__(self, key, data, left_node=None, right_node=None):
            self.key = key
            self.data = data
            self.left_node = left_node
            self.right_node = right_node

        def isLeaf(self):
            return not self.left_node and not self.right_node

        def hasLeft(self):
            return not (self.left_node is None)

        def hasRight(self):
            return not (self.right_node is None)


b = BinaryTree
b.Node(0, 0, b.Node(1, 1), b.Node(2, 2))
print(a.isLeaf())
print(a.hasLeft())
print(a.hasRight())


class Node():
    def __init__(self, x, left=None):
        self.val = x
        self.right = None


n = Node(0, Node(1))
n

class Solution(object):
    def invertTree(self, root):

        Node()

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
