# Name: Dylan Parson Student ID: 010674532

# imports
from HashTable import HashTable
from Package import Package
from LoadData import LoadData
from Truck import Truck
import datetime

# Function for getting distance between two addresses
# O(1)
def distanceBetween(address1, address2):
    return distanceList[addressList.index(address1)][addressList.index(address2)]

# O(N)
def minDistanceFrom(fromAddress, truckPackages):
    minDistance = 100.0
    index = 0
    for i in range(0, 16):
        temp = distanceBetween(fromAddress, truckPackages[i].address)
        # if the distance is less than the curent lowest, and the current packages has not been delivered
        if float(temp) < minDistance and truckPackages[i].status != 'DELIVERED':
            minDistance = float(temp)
            index = i
            # packageTable

    truckPackages[index].status = 'DELIVERED'
    return minDistance
def initialLoads():
    truck1.loadTruck(packageTable.search('1'))
    truck1.loadTruck(packageTable.search('2'))
    truck1.loadTruck(packageTable.search('4'))
    truck1.loadTruck(packageTable.search('5'))
    truck1.loadTruck(packageTable.search('7'))
    truck1.loadTruck(packageTable.search('8'))
    truck1.loadTruck(packageTable.search('10'))
    truck1.loadTruck(packageTable.search('11'))
    truck1.loadTruck(packageTable.search('12'))
    truck1.loadTruck(packageTable.search('17'))
    truck1.loadTruck(packageTable.search('21'))
    truck1.loadTruck(packageTable.search('22'))
    truck1.loadTruck(packageTable.search('23'))
    truck1.loadTruck(packageTable.search('24'))
    truck1.loadTruck(packageTable.search('26'))
    truck1.loadTruck(packageTable.search('27'))
    truck1.loadTruck(packageTable.search('29'))

    truck2.loadTruck(packageTable.search('3'))
    truck2.loadTruck(packageTable.search('9'))
    truck2.loadTruck(packageTable.search('13'))
    truck2.loadTruck(packageTable.search('14'))
    truck2.loadTruck(packageTable.search('15'))
    truck2.loadTruck(packageTable.search('16'))
    truck2.loadTruck(packageTable.search('18'))
    truck2.loadTruck(packageTable.search('19'))
    truck2.loadTruck(packageTable.search('20'))
    truck2.loadTruck(packageTable.search('30'))
    truck2.loadTruck(packageTable.search('31'))
    truck2.loadTruck(packageTable.search('33'))
    truck2.loadTruck(packageTable.search('34'))
    truck2.loadTruck(packageTable.search('35'))
    truck2.loadTruck(packageTable.search('36'))
    truck2.loadTruck(packageTable.search('38'))

def truckDeliverPackages(truck):
    if truck.miles < 70:
        milesToAddress = minDistanceFrom(truck.currentAddress, truck.packagesLoaded)
        truck.miles += milesToAddress
        timeToAddress = milesToAddress / 18
        truck.truckTime = datetime.time(int(timeToAddress))
        minutesToAddress = timeToAddress * 60
        

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

initialLoads()

for i in range(0, 15):
    truckDeliverPackages(truck1)
    truckDeliverPackages(truck2)

# This does not work because some packages do not get to hub until a certain time
# Look for packages with not special notes, going to use truck 2 for special notes since most need to be on there
# for i in range(1, 41):
#     temp = packageTable.search(str(i))
#     if temp.notes == '' and temp.status == '' and truck1.numCurrentPackages != 16:
#         truck1.loadTruck(packageTable.search(str(i)))
#     else:
#         # Prioritize special notes packages for initial loads
#         if temp.notes != '' and temp.status == '' and truck2.numCurrentPackages != 16:
#             truck2.loadTruck(packageTable.search(str(i)))
#         else:
#             if truck1.numCurrentPackages == 16 and temp.status == '':
#                 truck2.loadTruck(packageTable.search(str(i)))