# Name: Dylan Parson Student ID: 010674532

from HashTable import HashTable
from Package import Package
from LoadData import LoadData
from Truck import Truck

# Function for getting distance between two addresses
# O(1)
def distanceBetween(address1, address2):
    return distanceList[addressList.index(address1)][addressList.index(address2)]

# Function for loading truck
def loadTruck(truck, addressData, packageData, distanceData):
    print(addressData)

# Create truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# Initialize LoadData object
load = LoadData()

# Initialize hash table
packageTable = HashTable()

# Pass hash table in to have packages inserted
load.loadPackageData('WGUPS Package File.csv', packageTable)
# Load address list
addressList = load.loadAddressData('WGUPS Address Table.csv')
# Load distance list
distanceList = load.loadDistanceData('WGUPS Distance Table.csv')

loadTruck(truck1, addressList, packageTable, distanceList)

# for i in range(41):
#     packageTable.printValues(str(i))