#Create a Package python file

#Like the truck class, define the package object with def init and a def str

#In the Package object class I created a method to determine the package status of: at hub, en route, delivered - 7 lines of code

class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight, status):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.depart = None
        self.delivery = None

    def __str__(self):
        return f"{self.package_id} {self.address} {self.deadline} {self.city} \
            {self.zip_code} {self.weight} {self.status} {self.depart} {self.delivery}"      

    def status_report(self, convert_timedelta):
        if self.delivery < convert_timedelta:
            self.status = "Delivered!"
        elif self.depart > convert_timedelta:
            self.status = "En route!"
        else:
            self.status = "At Hub!"

#package ID number
#delivery address
#delivery deadline
#delivery city
#delivery zip code
#package weight
#delivery status (e.g., delivered, en route)