# Dylan Parson Student ID: 010674532
from HashTable import HashTable
from Package import Package
import csv

def loadDistanceData(file):
    with open(file) as distances:
        next(distances)
        distanceData = csv.reader(distances, delimiter=',')
        for distance in distanceData:
            # Load entire arrays into list
            mile = distance
            distanceList.append(mile)

def loadAddressData(file):
    with open(file) as addresses:
        next(addresses)
        addressData = csv.reader(addresses, delimiter=',')
        for address in addressData:
            aName = address
            addressList.append(aName)
def loadPackageData(file):
 with open(file) as packages:
     packageData = csv.reader(packages, delimiter=',')
     next(packageData)  # skip header
     for package in packageData:
         pId = int(package[0])
         pAddress = package[1]
         pCity = package[2]
         pState = package[3]
         pZip = package[4]
         pDeadline = package[5]
         pWeight = package[6]
         # check for special notes
         if package[7] is not None:
             pNotes = package[7]
         else:
             pNotes = None

         # create package object
         package = Package(pId, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes)
         # load package object into hash table
         packageTable.insert(str(package.id), package)

def distanceBetween(address1, address2):
    return distanceList[addressList.index(address1)][addressList.index(address2)]

# Initialize hash table
packageTable = HashTable()
# Initialize Address list
addressList = []
# Initialize Distance list
distanceList = []

# Load data from csv into packageTable
loadPackageData('WGUPS Package File.csv')
# Load data from csv into addressList
loadAddressData('WGUGPS Address Table.csv')
# Load data fro csv into distanceList
loadDistanceData('WGUPS Distance Table.csv')

print(addressList)
print(packageTable)
print(distanceList)
