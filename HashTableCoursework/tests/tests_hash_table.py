import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_insert(self):
        table = HashTable()

        table.insert('name', 'Ivan')

        self.assertEqual(list(table.items()), [('name', 'Ivan')])

    def test_duplicate_key(self):
        table = HashTable()
        table.insert('name', 'Ivan')

        with self.assertRaises(KeyError):
            table.insert('name', 'Vadim')

    def test_search(self):
        table = HashTable()
        table.insert('name', 'Ivan')

        value = table.search('name')

        self.assertEqual(value, 'Ivan')

    def test_search_missing(self):
        table = HashTable()
        table.insert('name', 'Ivan')

        value = table.search('age')

        self.assertIsNone(value)

    def test_collision(self):
        table = HashTable(hash_func=lambda x: abs(x))

        table.insert(1, "1")
        table.insert(-1, "2")

        self.assertEqual(table[1], '1')
        self.assertEqual(table[-1], '2')
        self.assertEqual(len(table), 2)

    def test_delete(self):
        table = HashTable()
        table.insert('name', 'Ivan')

        table.delete('name')

        self.assertEqual(len(table), 0)

    def test_delete_from_chain(self):
        table = HashTable(hash_func=lambda key: 0)
        table.insert('name', 'Ivan')
        table.insert('surname', 'Raviol')
        table.insert('number', 89121233333)

        table.delete('surname')

        self.assertEqual(list(table.items()), [('name', 'Ivan'), ('number', 89121233333)])

    def test_update_value(self):
        table = HashTable()
        table.insert('name', 'Ivan')
        
        table['name'] = 'Vadim'

        self.assertEqual(table['name'], 'Vadim')

    def test_resize(self):
        table = HashTable(capacity=2)

        table.insert('name', 'Ivan')
        table.insert('age', 20)
        table.insert('city', 'Moscow')

        self.assertEqual(len(list(table.get_view())), 4)

    def test_invalid_capacity(self):

        with self.assertRaises(ValueError):
            HashTable(capacity=0)

        with self.assertRaises(TypeError):
            HashTable(capacity=True)

        

        

