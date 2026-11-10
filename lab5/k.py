
import sys
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 10**9)
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key == node.key:
            return node

        if key < node.key:
            node.left = self._insert(node.left, key)

            if node.left.priority > node.priority:
                node = self.rotate_right(node)

        else:
            node.right = self._insert(node.right, key)

            if node.right.priority > node.priority:
                node = self.rotate_left(node)

        return node

    def next(self, key):
        node = self.root
        result = -1

        while node is not None:
            if node.key >= key:
                result = node.key
                node = node.left
            else:
                node = node.right

        return result


tree = Treap()

n = int(input())

last_answer = -1
previous_query = False

for _ in range(n):
    command, x = input().split()
    x = int(x)

    if command == "+":
        if previous_query:
            x = (x + last_answer) % (10**9)

        tree.insert(x)
        previous_query = False

    elif command == "?":
        last_answer = tree.next(x)
        print(last_answer)
        previous_query = True
