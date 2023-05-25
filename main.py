# Dylan Parson Student ID: 010674532
from HashTable import HashTable
import csv

# Class for Package
class Package:
    def __init__(self, id, address, city, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status


my_hash_table = HashTable()

my_hash_table.insert('1', 'Test')
my_hash_table.insert('2', 'Another test')
my_hash_table.insert('1', 'Testing')
my_hash_table.delete('2')
print(my_hash_table.search('1'))
# my_hash_table.print_table()
