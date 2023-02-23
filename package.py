#Create a Package python file

#Like the truck class, define the package object with def init and a def str

#In the Package object class I created a method to determine the package status of: at hub, en route, delivered - 7 lines of code

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

    def __str__(self):
        return f"{self.id}, {self.address}, {self.deadline}, {self.city}, {self.zip_code}, {self.weight}, {self.status} {self.depart}, {self.delivery}"  

    def status_report(self, converted_time):
        if self.depart > converted_time:
            self.status = "En route!"
        elif self.delivery < converted_time:
            self.status = "Delivered!"
        else:
            self.status = "At Hub!"

#package ID number
#delivery address
#delivery deadline
#delivery city
#delivery zip code
#package weight
#delivery status (e.g., delivered, en route)