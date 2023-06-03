# Class for Trucks

class Truck:
    def __init__ (self, packagesLoaded = 0, numCurrentPackages = 0, maxPackages = 16, miles = 0, currentAddress =''):
        self.packagesLoaded = []
        self.numCurrentPackages = 0
        self.maxPackages = 16
        self.miles = 0
        self.currentAddress = '4001 South 700 East'

    # Adds to end of list
    # O(N)
    def loadTruck(self, package):
        # If maximum packages has not already been reached
        if self.numCurrentPackages is not self.maxPackages:
            self.packagesLoaded.append(package)
            self.numCurrentPackages += 1
            package.status = 'LOADED'