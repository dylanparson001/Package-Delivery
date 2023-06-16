# Class for Trucks
import datetime
class Truck:
    def __init__(self, id, packagesLoaded = 0, numCurrentPackages = 0, maxPackages = 16, miles = 0, currentAddress ='',
                  truckTime = datetime.datetime(2023, 6, 8, 8, 0, 0)):
        self.id = id
        self.packagesLoaded = []
        self.numCurrentPackages = 0
        self.maxPackages = 16
        self.miles = 0
        self.currentAddress = '4001 South 700 East'
        self.truckTime = truckTime

    # Adds to end of list
    # O(1)
    def loadTruck(self, package):
        # If maximum packages has not already been reached
        if self.numCurrentPackages is not self.maxPackages and package.status == 'HUB':
            self.packagesLoaded.append(package)
            self.numCurrentPackages += 1
            package.status = 'LOADED'
            package.truckId = self.id
            package.loadTime = self.truckTime
            print()
