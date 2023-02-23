#Nearest neighbor algorithm to sort packages for shortest route
import csv
import datetime
from truck import Truck
from package import Package
from chain_hash import ChainHash

#read addresses csv file and make list called address_file
with open("csv_files.csv/address.csv", encoding = "utf-8-sig") as address_info:
    address_file = list(csv.reader(address_info))
    
#read distance csv file and make list that works as 2D array called distance_file
with open("csv_files.csv/distance.csv", encoding = "utf-8-sig") as distance_info:
    distance_file = list(csv.reader(distance_info, delimiter = ","))

#Method to load package objects into hash table
def load_pack_to_hash(file, hash_table):
    with open(file, encoding = "utf-8-sig") as pack_info:
        pack_data = csv.reader(pack_info)
        for package in pack_data:
            pack_id = int(package[0])
            pack_address = package[1]
            pack_city = package[2]
            pack_state = package[3]
            pack_zip_code = package[4]
            pack_deadline = package[5]
            pack_weight = package[6]
            pack_status = "At Hub!"

            #Create package objects with attributes read from csv file
            pack = Package(pack_id, pack_address, pack_city, pack_state, pack_zip_code, pack_deadline, pack_weight, pack_status)

            #insert key-values into hash table
            hash_table.insert(pack_id, pack)

#Method to obtain distance between two addresses
def distance_between(row, col):
    distance = distance_file[col][row]
    if distance == '':
        distance = distance_file[row][col]

    return float(distance)

#Method to obtain address from address_file (read from csv)
def get_address(address):
    for row in address_file:     
        if address in row[2]:
            return int(row[0])

    #if address not found, return the address that was not found        
    print("\"" + address + "\" not found!")      
    return -1

#Create truck objects, manually load packages to each, and set time of departure from main hub
truckA = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 21, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours = 8))

truckB = Truck(16, 18, None, [3, 6, 18, 19, 23, 24, 25, 26, 27, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5))

truckC = Truck(16, 18, None, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 22, 28, 32, 33, 35, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours = 10, minutes = 20))

#Create hash table
pack_hash_table = ChainHash()

#Load package objects with attributes read from csv file into hash table
load_pack_to_hash("csv_files.csv/package.csv", pack_hash_table)

#Method that implements nearest neighbor algorithm to sort packages in truck by shortest route
#Method also calculates total distances that the trucks travel
#total space-time complexity for algo O(N^3)
def deliver(truck):
    
    #Create array for all packages pending delivery and place them in array
    pending_delivery = []
    for package_id in truck.package: #O(N)
        package = pack_hash_table.find(package_id)
        pending_delivery.append(package)
    
    #Clear trucks of all packages to sort for reinsertion
    truck.package.clear()

    #Sort packages by calculating shortest distance from truck's current location
    #to location of nearest package address and then adds packages to truck list
    #by that order
    while len(pending_delivery) > 0: #O(N)
        closest_address = 3000
        next_package = None
        for package in pending_delivery:#O(N)
            truckAddress = get_address(truck.address)
            packageAddress = get_address(package.address)
            distance = distance_between(truckAddress, packageAddress)
            if distance <= closest_address:
                closest_address = distance
                next_package = package

        # add next nearest package to truck package list
        truck.package.append(next_package.id)

        # remove package from pending_delivery list
        pending_delivery.remove(next_package)

        # add miles traveled to next package address to truck miles attribute
        truck.miles += closest_address

        # update truck location to address of the package it traveled to
        truck.address = next_package.address

        # update time required for truck to arrive at nearest package location
        truck.time += datetime.timedelta(hours = closest_address / 18)
        next_package.delivery = truck.time
        next_package.depart = truck.departure_time

#Send trucks to deliver packages
deliver(truckA)
deliver(truckC)
deliver(truckB)
