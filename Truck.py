# Class for Trucks

class Truck:
    def __init__ (self, packagesLoaded = 0, numCurrentPackages = 0, maxPackages = 16):
        self.packagesLoaded = []
        self.numCurrentPackages = 0
        self.maxPackages = 16

    # Adds to end of list
    # O(N)
    def loadTruck(self, package):
        self.packagesLoaded.append(package)
        self.numCurrentPackages += 1