class Package:
    def __init__(self, id, address, city, zip, deadline, weight, notes, status, deliveredTime = 0, loadTime = 0):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.loadTime = loadTime
        self.deliveredTime = deliveredTime
        self.truckId = 0

    def printValues(self):
        print("ID:", self.id,  "\t", "Truck Id:",  self.truckId, "\t", "Status:", self.status, "\t", "Load Time:", self.loadTime,
              "\t", "Delivered Time:", self.deliveredTime, "\t", "Deadline:", self.deadline, "\t", "Address:", self.address,  "\t", "City:", self.city,  "\t", "Zip:", self.zip,  "\t",
                "Weight:", self.weight, "\t", "Notes:", self.notes)