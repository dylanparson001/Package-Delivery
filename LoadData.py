from HashTable import HashTable
from Package import Package
import csv

class LoadData:
    # O(N)
    def loadDistanceData(self, file):
        # Local list to be returned
        distanceList = []
        with open(file) as distances:
            next(distances) # skip header row
            distanceData = csv.reader(distances, delimiter=',')
            for distance in distanceData:
                # Set row of miles to be appended, creating a 2d matrix
                mile = distance
                distanceList.append(mile)
        return distanceList

    # O(N)
    def loadAddressData(self, file):
        addressList = []
        with open(file) as addresses:
            next(addresses)
            addressData = csv.reader(addresses, delimiter=',')
            for address in addressData:
                aName = address
                addressList.append(aName)
        return addressList

    # O(N)
    def loadPackageData(self, file, packageList):
     with open(file) as packages:
         packageData = csv.reader(packages, delimiter=',')
         next(packageData)  # skip header
         for package in packageData:
             # put data into their own variables for creating package objects
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
             package = Package(pId, pAddress, pCity, pZip, pDeadline, pWeight, pNotes, 'Not Delivered')
             # id, address, city, zip, deadline, weight, notes, status
             # load package object into hash table

             packageList.insert(str(package.id), package)
