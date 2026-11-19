from hash_functions import additive_hash


class HashTable:
    class Node:
        def __init__(self, key, value):

            self.key = key
            self.value = value
            self.next = None

        def __str__(self):

            return f'{self.key} -> {self.next}'
    def __init__(self, capacity=8, hash_func=additive_hash, auto_resize=True):

        if isinstance(capacity, bool) or not isinstance(capacity, int):
            raise TypeError("Вместимость должна быть целым числом")

        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной")
        
        self.__buckets = [None] * capacity
        self.__size = 0
        self.__hash_func = hash_func
        self.auto_resize = auto_resize

    def __getitem__(self, key): 

        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        _, node = self.__find_node(bucket, key)

        if node:
            return node.value

        raise KeyError(key)
    
    def __setitem__(self, key, value):
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        previous, node = self.__find_node(bucket, key)

        if node:
            node.value = value
            return
        
        alpha = self.__size / len(self.__buckets)

        if self.__auto_resize and alpha >= 1:
            self.__resize()
            self.insert(key, value)
            return
        
        if previous:
            previous.next = self.Node(key, value)
        else:
            self.__buckets[index] = self.Node(key, value)
        self.__size += 1

    def __contains__(self, key):
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        _, node = self.__find_node(bucket, key)
        return bool(node)


    def __iter__(self):
        for bucket in self.__buckets:
            for node in self.__iter_bucket(bucket):
                yield node.key

    def __len__(self):
        return self.__size

    def insert(self, key, value):
        """Добавляет новую пару ключ–значение в хеш-таблицу.

        Входные данные:
            key: Ключ нового элемента.
            value: Значение нового элемента.

        Возвращаемое значение:
            None.

        Исключения:
            KeyError: Если указанный ключ уже существует.
        """
        
        # Делаем рехеширование
        alpha = self.__size /  len(self.__buckets)
        
        # Расширяем таблицу перед превышением коэффициента загрузки 1.
        if self.__auto_resize and alpha >= 1:
            self.__resize()
            
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        previous, node = self.__find_node(bucket, key)
        
        if not previous and not node:
            self.__buckets[index] = self.Node(key, value)
        elif not node:
            previous.next = self.Node(key, value)
        else: 
            raise KeyError(f"Ключ {key} уже существует")
        
        self.__size += 1

    def items(self):
        """Последовательно перебирает пары ключ–значение таблицы.

        Входные данные:
            Нет.

        Возвращаемое значение:
            iterator: Итератор по кортежам (key, value).
        """
        for bucket in self.__buckets:
            for node in self.__iter_bucket(bucket):
                yield (node.key, node.value)

    def search(self, key):
        """Ищет значение, связанное с указанным ключом.

        Входные данные:
            key: Искомый ключ.

        Возвращаемое значение:
            Значение найденного элемента или None, если ключ отсутствует.
        """
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        _, node = self.__find_node(bucket, key)

        if node:
            return node.value
        
        return None
    
    def delete(self, key):
        """Удаляет элемент с указанным ключом, если он существует.

        Входные данные:
            key: Ключ удаляемого элемента.

        Возвращаемое значение:
            None.
        """
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        previous, node = self.__find_node(bucket, key)

        if not node:
            return 
        
        if not previous:
            self.__buckets[index] = node.next
        else:
            previous.next = node.next

        self.__size -= 1

    def get_view(self):
        """Формирует представление содержимого всех корзин таблицы.

        Входные данные:
            Нет.

        Возвращаемое значение:
            list(list[tuple]): Список корзин с кортежами (key, value).
        """
        return [
            [(node.key, node.value) for node in self.__iter_bucket(bucket)]
            for bucket in self.__buckets
        ]

    @property
    def auto_resize(self):
        """Показывает, включено ли автоматическое увеличение числа корзин.

        Входные данные:
            Нет.

        Возвращаемое значение:
            bool: True, если автоматическое расширение включено, иначе False.
        """
        return self.__auto_resize

    @auto_resize.setter
    def auto_resize(self, enabled):
        """Включает или отключает автоматическое расширение таблицы.

        Входные данные:
            enabled (bool): Новое состояние автоматического расширения.

        Возвращаемое значение:
            None.
        """
        if not isinstance(enabled, bool):
            raise TypeError("Переключатель рехеширования должен иметь тип bool")
        self.__auto_resize = enabled

    def __get_hash(self, key):
        """Вычисляет индекс корзины для указанного ключа.

        Входные данные:
            key: Ключ, для которого требуется определить корзину.

        Возвращаемое значение:
            int: Индекс корзины в диапазоне размеров таблицы.
        """
        return self.__hash_func(key) % len(self.__buckets)

    def __find_node(self, bucket, key):
        """Ищет узел с указанным ключом внутри цепочки корзины.

        Входные данные:
            bucket (Node | None): Первый узел цепочки корзины.
            key: Искомый ключ.

        Возвращаемое значение:
            tuple[Node | None, Node | None]: Предыдущий и найденный узлы.
            Если ключ не найден, второй элемент равен None, а первый содержит
            последний узел цепочки либо None для пустой корзины.
        """

        previous = None

        for node in self.__iter_bucket(bucket):
            if node.key == key:
                return previous, node
            
            previous = node
        return previous, None

    def __iter_bucket(self, bucket):
        """Последовательно перебирает узлы одной корзины.

        Входные данные:
            bucket (Node | None): Первый узел цепочки корзины.

        Возвращаемое значение:
            iterator: Итератор по узлам цепочки.
        """
        current = bucket
        while current:
            yield current
            current = current.next

    def __resize(self):
        """Удваивает число корзин и заново распределяет все элементы.

        Входные данные:
            Нет.

        Возвращаемое значение:
            None.
        """
        new_buckets = [None] * len(self.__buckets) * 2
        old_buckets = self.__buckets
        self.__buckets = new_buckets
        self.__size = 0
        for b in old_buckets:
            for node in self.__iter_bucket(b):
                self.insert(node.key, node.value)
                
            
