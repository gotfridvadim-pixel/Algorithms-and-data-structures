from hash_table import*
from hash_functions import*


def main():
    def get_hash(key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            return additive_hash(key)
        else:
            raise TypeError('Непподерживаемый тип ключа')

    table = HashTable(auto_resize=False)
    table.insert('1', 'Ivan')
    table.insert('2', 'Raviol')
    table.insert('3', 89121233333)

    table['key'] = 'key'
    print(table.get_view())


    
if __name__ == '__main__':
    
    main()
    
    

    
