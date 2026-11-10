
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

    # Вставка
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
            
    def _inorder(self, node):
        if node is None:
            return

        yield from self._inorder(node.left)
        yield node
        yield from self._inorder(node.right)


    # Развилки: два потомка
    def print_branches(self):
        for node in self._inorder(self.root):
            if node.left is not None and node.right is not None:
                print(node.data, sep="\n")


tree = BinaryTree()

for x in map(int, sys.stdin.read().split()):
    if x == 0:
        break

    tree.add(x)

tree.print_branches()
