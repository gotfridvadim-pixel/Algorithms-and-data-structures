
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
            
    # Количество элементов
    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0

        return 1 + self._count(node.left) + self._count(node.right)

tree = BinaryTree()

for x in map(int, sys.stdin.read().split()):
    if x == 0:
        break

    tree.add(x)


print(tree.count())