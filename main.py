# Dylan Parson Student ID: 010674532
from HashTable import HashTable
from Package import Package
import csv

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
         if package[7] is not None:
             pNotes = package[7]
         else:
             pNotes = None

             # create package object
         package = Package(pId, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes)

         package_table.insert(str(package.id), package)

package_table = HashTable()

loadPackageDataa('WGUPSPackageFile.csv')

print(package_table.search('27'))

package_table.print_table()
