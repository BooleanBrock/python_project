#Create a Package python file

#Like the truck class, define the package object with def init and a def str

#In the Package object class I created a method to determine the package status of: at hub, en route, delivered - 7 lines of code

#create class for package objects
class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.depart = None
        self.delivery = None

#Create method to return string containing attributes of package object
    def __str__(self):
        return f"{self.id}, {self.address}, {self.city}, {self.zip_code}, {self.weight}, {self.deadline}, {self.status}, {self.depart}, {self.delivery}"  

#Create method to report status of package at any given time in delivery process
    def status_report(self, converted_time):
        if self.delivery < converted_time:
            self.status = "Delivered!"
        elif self.depart < converted_time:
            self.status = "En route!"
        elif self.depart > converted_time:
            self.status = "At Hub!"
