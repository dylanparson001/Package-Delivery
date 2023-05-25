# Hash table class E.  Develop a hash table, without using any additional libraries or classes, that has an insertion
# function that takes the following components as input and inserts the components into the hash table
class HashTable:
    # Constructor with a default size of 40
    def __init__(self, size = 40):
        self.data_map = [None] * size
    # Hashing algorithm
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    #Prints the entire hash table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ",  val)
    
    #Adds item to the hash table, key is the package ID number
    def insert(self, key, value):
        index = self.__hash(key)    
        
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    # Gets item based on key
    def search(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]
        for item in bucket:
            if item[0] == key:
                return item
        # index = self.__hash(key)
        # if self.data_map[index] is not None:
        #     for i in range(len(self.data_map[index])):
        #         if self.data_map[index][i][0] == key:
        #             return self.data_map[index]
        # If you get to this point there is no item with that key
        return None
    # Removes value from table given key
    def delete(self, key):
        index = self.__hash(key)
        bucket = self.data_map[index]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)

    def printValues(self, key):
        example = self.get_item(key)
        print("ID: ", example[1].id, " Address: ", example[1].address, " City: ", example[1].city, " Zip: ", example[1].zip, " Deadline: ", example[1].deadline,
              " Weight: ", example[1].weight, " Notes: ", example[1].notes, " Status: ", example[1].status)

       