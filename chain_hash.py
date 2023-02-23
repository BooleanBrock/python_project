#Create a "create hash map" Python file
class ChainHash:
    def __init__(self, starting_capacity = 20):
        self.table = []
        for i in range(starting_capacity):
            self.table.append([])

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for key_val in bucket_list:
            if key_val[0] == key:
                key_val[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
                   
    def find(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for match in bucket_list:
            if key == match[0]:
                return match[1]
        return None

    def remove(self, key):
        bucket = hash(key) & len(self.table)
        bucket_list = self.table[bucket]
        if key in bucket_list:
            bucket_list.remove(key)
