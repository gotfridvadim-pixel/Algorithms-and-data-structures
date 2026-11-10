
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        node = self.root

        while True:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                    return
                node = node.left

            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                    return
                node = node.right

            else:
                return

    # Высота дерева
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0

        left = self._height(node.left)
        right = self._height(node.right)

        return max(left, right) + 1


tree = BinaryTree()

for x in map(int, sys.stdin.read().split()):
    if x == 0:
        break

    tree.add(x)


print(tree.height())