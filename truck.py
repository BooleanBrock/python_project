#Create class for truck object
class Truck:
    def __init__(self, capacity, speed, load, package, miles, address, departure_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.package = package
        self.miles = miles
        self.address = address
        self.departure_time = departure_time
        self.time = departure_time

#Create method to return string containing attributes of truck object
    def __str__(self):
        return f"{self.capacity}, {self.speed}, {self.load}, {self.package}, {self.miles}, {self.address}, {self.departure_time}"