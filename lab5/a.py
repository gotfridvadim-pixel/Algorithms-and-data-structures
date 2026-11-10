
import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.get_data():
            if node.get_left() is None:
                node.set_left(Node(data))
            else:
                self._add(data, node.get_left())

        elif data > node.get_data():
            if node.get_right() is None:
                node.set_right(Node(data))
            else:
                self._add(data, node.get_right())

    def search(self, data):
        if self.root is not None:
            return self._search(data, self.root)
        else:
            return False

    def _search(self, data, node):
        if data == node.get_data():
            return True

        elif data < node.get_data() and node.get_left() is not None:
            return self._search(data, node.get_left())

        elif data > node.get_data() and node.get_right() is not None:
            return self._search(data, node.get_right())

        return False

    def delete(self, data):
        if self.root is None:
            return
        else:
            self.root = self._delete(data, self.root)

    def _delete(self, data, parent):
        if parent is None:
            return None

        # Поиск удаляемого узла
        if data < parent.get_data():
            parent.set_left(self._delete(data, parent.get_left()))

        elif data > parent.get_data():
            parent.set_right(self._delete(data, parent.get_right()))

        else:
            # 0 детей
            if parent.get_left() is None and parent.get_right() is None:
                return None

            # 1 ребёнок (только правый)
            elif parent.get_left() is None:
                return parent.get_right()

            # 1 ребёнок (только левый)
            elif parent.get_right() is None:
                return parent.get_left()

            # 2 ребёнка
            else:
                max_node = self._find_max(parent.get_left())
                parent.data = max_node.get_data()

                parent.set_left(
                    self._delete(max_node.get_data(), parent.get_left())
                )

        return parent

    # Поиск максимального элемента поддерева
    def _find_max(self, node):
        while node.get_right() is not None:
            node = node.get_right()
        return node

    # Вывод дерева
    def pprint(self):
        self._pprint(self.root, 0)

    def _pprint(self, node, level):
        if node is None:
            return

        self._pprint(node.get_left(), level + 1)

        print("." * level + str(node.get_data()))

        self._pprint(node.get_right(), level + 1)



tree = BinaryTree()

for line in sys.stdin:
    command = line.split()

    if command[0] == "ADD":
        data = int(command[1])

        if tree.search(data):
            print("ALREADY")
        else:
            tree.add(data)
            print("DONE")

    elif command[0] == "DELETE":
        data = int(command[1])

        if tree.search(data):
            tree.delete(data)
            print("DONE")
        else:
            print("CANNOT")

    elif command[0] == "SEARCH":
        data = int(command[1])

        if tree.search(data):
            print("YES")
        else:
            print("NO")

    elif command[0] == "PRINTTREE":
        tree.pprint()
