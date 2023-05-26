# Class for Trucks

class Truck:
    packagesLoaded = []
    def __init__ (self, id, miles = 0, currentPackages = 0, maximumPackages = 16):
        self.id = id
        self.miles = miles
        self.currentPackages = currentPackages
        self.maximumPackages = maximumPackages

    def loadTruck(self, package):
        packages.append(package)