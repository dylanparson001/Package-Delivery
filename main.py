# Name: Dylan Parson Student ID: 010674532

# imports
from HashTable import HashTable
from Package import Package
from LoadData import LoadData
from Truck import Truck
import datetime
from datetime import timedelta

# Function for getting distance between two addresses
# O(1)
def distanceBetween(address1, address2):
    distance = float(distanceList[addressList.index(address1)][addressList.index(address2)])
    return distance

# O(N)
# Main algorithm for delivering packages loaded onto trucks, searches for minimum distance from current address
# then saves the delivery time and status on the package
def truckDeliverPackages(truck):
    # if the truck has no packages, don't continue with function
    if truck.numCurrentPackages == 0:
        return

    # Default value to test against distances
    minDistance = 100.0

    # will be used to deliver the correct package after checking
    index = 0

    # some packages do not get to depot until 9:05AM
    timePackagesAtDepot = datetime.datetime(2023, 6, 8, 9, 5, 0)
    # Time for package 9 for the address to be corrected
    timeAddressFixed = datetime.datetime(2023, 6, 8, 9, 0, 0)
    # time to focus on items with 10:30AM deadline to ensure they get there before the deadline
    timeDeadlines = datetime.datetime(2023, 6, 8, 8, 45, 0)

    # Loops through all packages on truck, checking for certain conditions, leaving the loop if certain conditions are met
    # O(N)
    for i in range(0, truck.numCurrentPackages):
        # get miles to the next package in list
        milesToTravel = distanceBetween(truck.currentAddress, truck.packagesLoaded[i].address)

        # if the nearest address in the list is the same address, deliver together to save miles and time
        if minDistance == 0.0:
            index = i
            truck.packagesLoaded[i].status = 'DELIVERED'
            truck.currentAddress = truck.packagesLoaded[i].address
            break

        # Prioritize packages with a 10:30 deadline after a certain time
        if truck.truckTime >= timeDeadlines and truck.packagesLoaded[i].deadline == '10:30 AM' and truck.packagesLoaded[i].status != 'DELIVERED':
            milesToTravel = distanceBetween(truck.currentAddress, truck.packagesLoaded[i].address)
            minDistance = milesToTravel
            index = i
            break

        # if you get here, whichever package is closest will be delivered
        if milesToTravel < minDistance:
            minDistance = milesToTravel
            index = i
    if truck.packagesLoaded[index].id == 9 and truck.truckTime < timeAddressFixed and truck.numCurrentPackages == 1:
        return
    # Deliver the packages and set current address to the delivered address
    truck.packagesLoaded[index].status = 'DELIVERED'
    truck.currentAddress = truck.packagesLoaded[index].address

    # Calculate time by 18mph speed in hours
    timeToAddress = minDistance / 18

    # time * 60 to get minutes
    minutesToAddress = timeToAddress * 60

    # add time to the truck time
    truck.truckTime = truck.truckTime + timedelta(minutes=minutesToAddress)

    # Set delivered time to package
    truck.packagesLoaded[index].deliveredTime = truck.truckTime

    truck.miles += minDistance
    truck.numCurrentPackages -= 1
    truck.packagesLoaded.pop(index)
    if truck.truckTime >= timePackagesAtDepot and packageTable.search('6').status != 'en route' and packageTable.search('25').status != 'LOADED' and packageTable.search('28').status != 'en route' and packageTable.search('32').status != 'en route':
        truck.loadTruck(packageTable.search('6'))
        truck.loadTruck(packageTable.search('25'))
        truck.loadTruck(packageTable.search('28'))
        truck.loadTruck(packageTable.search('32'))


# sends the truck to the hub
# O(1)
def goToHub(truck):
    distance = distanceBetween(truck.currentAddress, addressList[0])
    truck.currentAddress = addressList[0]
    truck.miles += distance

# Loads truck with the given package, checking for certain conditions
# O(N)
def loadTruck(truck):
    goToHub(truck)
    # Used to check for when certain packages will be at depot for pickup
    timePackagesAtDepot = datetime.datetime(2023, 6, 8, 9, 5, 0)

    # loops through all packages that are still at the hub
    for i in range(0, len(packagesAtHub)):

        # if the truck is fully loaded, do not attempt to load anymore
        if truck.numCurrentPackages == 16:
            return
        if packagesAtHub[i] != 'en route' and packagesAtHub[i] != 'DELIVERED':

            # if the package has been loaded, skip it
            if packagesAtHub[i] is not None and packagesAtHub[i].status != 'en route':
                # if it is after 9:05 get packages from depot
                if truck.truckTime >= timePackagesAtDepot:
                    truck.loadTruck(packageTable.search('6'))
                    truck.loadTruck(packageTable.search('25'))
                    truck.loadTruck(packageTable.search('28'))
                    truck.loadTruck(packageTable.search('32'))

                # if it is after the time that certain packages get delivered to depot
                if packagesAtHub[i] is not None and packagesAtHub[i].notes == 'Delayed on flight---will not arrive to depot until 9:05 am' and truck.truckTime <= timePackagesAtDepot:
                    continue
                elif packagesAtHub[i] is not None and packagesAtHub[i].notes == 'Delayed on flight---will not arrive to depot until 9:05 am' and truck.truckTime >= timePackagesAtDepot:
                    truck.loadTruck(packagesAtHub[i])
                    loadedPackages.append(packagesAtHub[i])
                    return

                # prioritize packages with a deadline
                elif packagesAtHub[i] is not None and packagesAtHub[i].deadline != 'EOD':
                    truck.loadTruck(packagesAtHub[i])
                    loadedPackages.append(packagesAtHub[i])

                elif packagesAtHub[i] is not None and packagesAtHub[i].deadline == 'EOD':
                    truck.loadTruck(packagesAtHub[i])
                    loadedPackages.append(packagesAtHub[i])


#G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)

def userInterface():
    userInput = 100

    while userInput != 0:

        print('************* WGUPS DELIVERY SERVICE *************')
        print('1. Print All Package Status and Total Mileage')
        print('2. Choose a time to view a package')
        print('3. Show miles travelled by all trucks')
        print('0. QUIT')

        userInput = int(input())

        match userInput:
            case 1:
                for i in range(1, 41):
                    packageTable.search(str(i)).printValues()
            case 2:
                print('What is the id of the package you want to see?')
                idToSearch = int(input())

                if idToSearch < 0 or idToSearch > 40:
                    print('out of range')
                else:
                    packageTable.search(str(idToSearch)).printValues()
            # total mileage traveled by all trucks
            case 3:
                print('Truck 1: ', truck1.miles)
                print('Truck 2: ', truck2.miles)
                print('Truck 3: ', truck3.miles)
                print('Total miles travelled: ', truck1.miles + truck2.miles + truck3.miles)
                pause = input()
            case 0:
                print('bye')
            case _:
                print('not an option')

def initialLoads():
    truck2.loadTruck(packageTable.search('3'))
    truck2.loadTruck(packageTable.search('18'))
    truck2.loadTruck(packageTable.search('36'))
    truck2.loadTruck(packageTable.search('38'))

    truck2.loadTruck(packageTable.search('13'))
    truck2.loadTruck(packageTable.search('14'))
    truck2.loadTruck(packageTable.search('15'))
    truck2.loadTruck(packageTable.search('16'))
    truck2.loadTruck(packageTable.search('19'))
    truck2.loadTruck(packageTable.search('20'))

    # To ensure deadlines are met packages with deadlines should be on either truck 1 or 2, truck 3 will get the leftovers
    truck2.loadTruck(packageTable.search('1'))
    truck2.loadTruck(packageTable.search('6'))
    truck2.loadTruck(packageTable.search('31'))

    truck1.loadTruck(packageTable.search('40'))
    truck1.loadTruck(packageTable.search('37'))
    truck1.loadTruck(packageTable.search('34'))
    truck1.loadTruck(packageTable.search('29'))
    truck1.loadTruck(packageTable.search('30'))
    truck1.loadTruck(packageTable.search('25'))

    loadTruck(truck1)
    loadTruck(truck2)
    loadTruck(truck3)

# Main program
# Create Truck objects
# Initial loads, making sure special notes are met and packages with deadlines are loaded before others

startTime = datetime.datetime(2023, 6, 8, 8, 0, 0)

truck1 = Truck(1)
truck1.truckTime = startTime

truck2 = Truck(2)
truck2.truckTime = startTime

truck3 = Truck(3)
truck3.truckTime = startTime

# Initialize LoadData object
load = LoadData()

# Initialize hash table
packageTable = HashTable()

# Get data from csv files
# O(N^3)
load.loadPackageData('WGUPS Package File.csv', packageTable)
addressList = load.loadAddressData('WGUPS Address Table.csv')
distanceList = load.loadDistanceData('WGUPS Distance Table.csv')

packagesAtHub = []
loadedPackages = []
deliveredPackages = []

# O(N)
for i in range(1, 41):
    packagesAtHub.append(packageTable.search(str(i)))

initialLoads()

# O(N^3)
for j in range(0, 50):
    truckDeliverPackages(truck1)
    truckDeliverPackages(truck2)
    # after trucks are done with their routes, one driver goes to other truck
    if truck1.numCurrentPackages == 0 or truck2.numCurrentPackages == 0:

        if truck1.truckTime < truck2.truckTime:
            truck3.truckTime = truck1.truckTime
        else:
            truck3.truckTime = truck2.truckTime
        truckDeliverPackages(truck3)

userInterface()