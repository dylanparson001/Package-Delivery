class Package:
    def __init__(self, id, address, city, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def printValues(self):
        print("ID: ", self.id, " Address: ", self.address, " City: ", self.city, " Zip: ", self.zip,
              " Deadline: ", self.deadline,
              " Weight: ", self.weight, " Notes: ", self.notes, " Status: ", self.status)