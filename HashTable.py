# Hash table class
# E.  Develop a hash table, without using any additional libraries or classes, that has an insertion
# function that takes the following components as input and inserts the components into the hash table
class HashTable:
    # Constructor with a default size of 30
    # originally set to 40, with 30 there are more rows with one item, thus making those lookups faster
    # when it was at 40, there were more empty rows and more rows with 3+ packages in, which is less efficient
    def __init__(self, size = 30):
        self.data_map = [None] * size
    # Hashing algorithm
    # O(N)
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    #Prints the entire hash table
    # O(N)
    def print_table(self):
        for i, val in enumerate(self.data_map):
            package = self.search(str(i))
            if(package is not None):
                package.printValues()
            # print(i, ": ",  val)
    
    #Adds item to the hash table, key is the package ID number
    # O(1)
    def insert(self, key, value):
        index = self.__hash(key)    
        
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    # F.  Develop a look-up function that takes the following components as input and returns the corresponding
    #  data elements:
    # Gets item based on key
    # O(1) if there is only one item in a bucket, O(N) if there are multiple

    def search(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]
        if bucket is not None:
            for item in bucket:
                if item[0] == key:
                    return item[1]
        # If you get to this point there is no item with that key
        return None
    # Removes value from table given key
    # O(1) if there is only one item in a bucket, O(N) if there are multiple
    def delete(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
    # O(1) if there is only one item in a bucket, O(N) if there are multiple
    def printValues(self):
        example = self.search(key)
        if example is not None:
            print("ID: ", self.example.id, " Address: ", self.example.address, " City: ", self.example.city, " Zip: ",
                  self.example.zip, " Deadline: ", self.example.deadline,
                  " Weight: ", self.example.weight, " Notes: ", self.example.notes, " Status: ", self.example.status)