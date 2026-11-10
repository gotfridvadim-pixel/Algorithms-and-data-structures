
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

    # Второй максимум
    def second_max(self):
        node = self.root
        parent = None

        while node.right is not None:
            parent = node
            node = node.right

        if node.left is not None:
            node = node.left

            while node.right is not None:
                node = node.right

            return node.data

        return parent.data

    



tree = BinaryTree()

for x in map(int, sys.stdin.read().split()):
    if x == 0:
        break

    tree.add(x)

print(tree.second_max())
