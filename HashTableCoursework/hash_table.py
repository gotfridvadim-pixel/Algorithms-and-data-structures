from hash_functions import additive_hash


class HashTable:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

        def __str__(self):
            return f'{self.key} -> {self.next}'

    def __init__(self, capacity=8, hash_func=additive_hash):
        if isinstance(capacity, bool) or not isinstance(capacity, int):
            raise TypeError("Вместимость должна быть целым числом")

        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительной")
        
        self.__buckets = [None] * capacity
        self.__size = 0
        self.__hash_func = hash_func

    # Перегрузка извлечения []
    def __getitem__(self, key): 
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        _, node = self.__find_node(bucket, key)

        if node:
            return node.value

        raise KeyError(key)
    
    # Перегрузка присвоения по []
    def __setitem__(self, key, value):
        """Добавляет новый ключ или обновляет существующий."""
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        previous, node = self.__find_node(bucket, key)

        if node:
            node.value = value
            return
        
        alpha = self.__size / len(self.__buckets)

        if alpha >= 1:
            self.__resize()
            self.insert(key, value)
            return
        
        if previous:
            previous.next = self.Node(key, value)
        else:
            self.__buckets[index] = self.Node(key, value)
        self.__size += 1

    # Перегрузка in
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
        
        # Делаем рехеширование
        alpha = self.__size /  len(self.__buckets)
        
        # Расширяем таблицу перед превышением коэффициента загрузки 1.
        if alpha >= 1:
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
        for bucket in self.__buckets:
            for node in self.__iter_bucket(bucket):
                yield (node.key, node.value)


    def search(self, key):
        index = self.__get_hash(key)
        bucket = self.__buckets[index]
        _, node = self.__find_node(bucket, key)

        if node:
            return node.value
        
        return None
    
    def delete(self, key):
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
        """Возвращает список корзин с парами (key, value)."""
        return [
            [(node.key, node.value) for node in self.__iter_bucket(bucket)]
            for bucket in self.__buckets
        ]

    def __get_hash(self, key):
        return self.__hash_func(key) % len(self.__buckets)

    def __find_node(self, bucket, key):
        """Возвращает предыдущий и найденный узлы либо пару (None, None)."""

        previous = None

        for node in self.__iter_bucket(bucket):
            if node.key == key:
                return previous, node
            
            previous = node
        return previous, None

    def __iter_bucket(self, bucket):
        """Перебор узлов внутри корзины."""
        current = bucket
        while current:
            yield current
            current = current.next

    def __resize(self):
        new_buckets = [None] * len(self.__buckets) * 2
        old_buckets = self.__buckets
        self.__buckets = new_buckets
        self.__size = 0
        for b in old_buckets:
            for node in self.__iter_bucket(b):
                self.insert(node.key, node.value)
                
            
