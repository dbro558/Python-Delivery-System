

# HashTable class

class HashTable:

    # Constructor
    # Complexity is O(1)
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Function to get hash, for use in other functions in HashTable class
    # Complexity is O(1)
    def _get_hash(self, key):
        bucket = hash(key) % len(self.table)
        return bucket

    # Insert new item into hash table
    # Complexity is O(n)
    def insert(self, key, value):
        key_hash = self._get_hash(key)  # O(1)
        key_value = [key, value]  # O(1)

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])  # O(1)
            return True  # O(1)
        else:
            for pair in self.table[key_hash]:  # O(n)
                if pair[0] == key:
                    pair[1] == value  # O(1)
                    return True  # O(1)
            self.table[key_hash].append(key_value)  # O(1)
            return True  # O(1)

    # Lookup function
    # Complexity is O(n)
    def lookup(self, key):
        key_hash = self._get_hash(key)  # O(1)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:  # O(n)
                if pair[0] == key:  # O(1)
                    return pair[1]  # O(1)
        return None

    # Delete function
    # Complexity is O(n)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.table[key_hash] is None:
            return False
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True
