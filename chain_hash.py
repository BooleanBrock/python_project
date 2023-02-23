#Create a "create hash map" Python file
#Citation Source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
class ChainHash:
    #create an empty table with starting amount of 20 and create empty buckets
    def __init__(self, starting_capacity = 20):
        self.table = []
        for i in range(starting_capacity):
            self.table.append([])
    
    #create method to insert and update numbers in hash table
    def insert(self, key, item):

        #get bucket to insert number
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        
        #update key value if key is already in bucket 
        for key_val in bucket_list: #O(N) CPU time
            #print key value after update
            if key_val[0] == key:
                key_val[1] = item
                return True

        #if key not already in hash table then add key and value to end of bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

       #find key and value in hash table and return value from matching bucket if found            
    def find(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for match in bucket_list:
            if key == match[0]:
                return match[1]
        
        return None #if match[0] does not match key
    
    #Method to remove key from hash table
    def remove(self, key):
        bucket = hash(key) & len(self.table)
        bucket_list = self.table[bucket]

        #if key found, then key is removed
        if key in bucket_list:
            bucket_list.remove(key)
