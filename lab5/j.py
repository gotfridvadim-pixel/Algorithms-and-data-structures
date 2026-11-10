
import sys


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.count = 1


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
                node.count += 1
                return

    def print_tree(self):
        stack = []
        node = self.root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()

            print(node.data, node.count)

            node = node.right


tree = BinaryTree()

for x in map(int, sys.stdin.read().split()):
    if x == 0:
        break

    tree.add(x)

tree.print_tree()
