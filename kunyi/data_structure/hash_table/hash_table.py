"""
hash table contains key value pairs that are supposed to be distributed to buckets evenly
it is designed to loop up in constant times

What if there is conflict? 1. Separate Chaining 2. Linear Probing(move slot one by one)
"""

#  1. Separate Chaining  In each slot, it's a linked list of HashEntry


class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_entry = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hashing_function(self, key):
        return hash(key) % self.size

    def rehash(self, entry, key, value):
        while entry and entry.key != key:
            prev, entry = entry, entry.next_entry
        # overwrite
        if entry:
            entry.value = value
        else:
            prev.next_entry = HashEntry(key, value)
        print('REHASHING')

    def set(self, key, value):
        hash_code = self.hashing_function(key)
        if self.table[hash_code] is None:
            self.table[hash_code] = HashEntry(key, value)
        else:
            self.rehash(self.table[hash_code], key, value)

    def get(self, key):
        hash_code = self.hashing_function(key)
        if self.table[hash_code] is None:
            raise KeyError
        entry = self.table[hash_code]
        while entry and entry.key != key:
            entry = entry.next_entry

        return entry.value


# Linear Probing(move slot one by one), two arrays for slot
class HashTable_Second:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hashing_function(self, key):
        return hash(key) % self.size

    def get_slot(self, key):
        slot = self.hashing_function(key)
        while self.keys[slot] and self.keys[slot] != key:
            # linear probing (make sure)
            slot = self.hashing_function(slot + 1)

        return slot

    def set(self, key, value):
        slot = self.get_slot(key)
        # slot is ind
        self.keys[slot] = key
        self.values[slot] = value

    def get(self, key):
        slot = self.get_slot(key)
        if not self.values[slot]:
            raise KeyError
        return self.values[slot]


if __name__ == '__main__':
    # hash_table = HashTable(10)
    # hash_table.set('test-1', 3434)
    # hash_table.set('test-3', 45)
    # hash_table.set('test-2', 343)
    # hash_table.set('test-6', 123)
    # print(hash_table.get('test-3'))
    # print(hash_table.get('test-2'))
    # # print(hash_table.get('test-7'))
    # hash_table.set('test-7', 123)
    # print(hash_table.get('test-7'))

    hash_table = HashTable_Second(10)
    hash_table.set('test-1', 3434)
    hash_table.set('test-3', 45)
    hash_table.set('test-2', 343)
    hash_table.set('test-6', 123)
    print(hash_table.get('test-3'))
    print(hash_table.get('test-2'))
    # print(hash_table.get('test-7'))
    hash_table.set('test-7', 123)
    print(hash_table.get('test-7'))
