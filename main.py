import csv
import datetime
from builtins import ValueError
from truck import Truck
from package import Package
from chain_hash import ChainHash

with open("csv_files.csv/address.csv", encoding = "utf-8-sig") as address_info:
    address_file = csv.reader(address_info)
    address_file = list(address_file)

with open("csv_files.csv/distance.csv", encoding = "utf-8-sig") as distance_info:
    distance_file = csv.reader(distance_info, delimiter = ",")
    distance_file = list(distance_file)

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

            pack = Package(pack_id, pack_address, pack_city, pack_state, pack_zip_code, pack_deadline, pack_weight, pack_status)

            hash_table.insert(pack_id, pack)

def distance_between(row, col):
    distance = distance_file[col][row]
    if distance == '':
        distance = distance_file[row][col]

    return float(distance)

def get_address(address):
    for row in address_file:     
        if address in row[2]:
            return int(row[0])
    print("\"" + address + "\" not found!")      
    return -1


truckA = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 21, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours = 8))

truckB = Truck(16, 18, None, [3, 6, 18, 19, 23, 24, 25, 26, 27, 36, 38], 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5))

truckC = Truck(16, 18, None, [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 22, 28, 32, 33, 35, 39], 0.0, "4001 South 700 East", datetime.timedelta(hours = 10, minutes = 20))

pack_hash_table = ChainHash()

load_pack_to_hash("csv_files.csv/package.csv", pack_hash_table)

def deliver(truck):
    pending_delivery = []
    for package_id in truck.package:
        package = pack_hash_table.find(package_id)
        pending_delivery.append(package)

    truck.package.clear()

    while len(pending_delivery) > 0:
        closest_address = 3000
        next_package = None
        for package in pending_delivery:
            truckAddress = get_address(truck.address)
            packageAddress = get_address(package.address)
            if distance_between(truckAddress, packageAddress) <= closest_address:
                closest_address = distance_between(truckAddress, packageAddress)
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

deliver(truckA)
deliver(truckC)
#truckB.departure_time = min(truckA.time, truckC.time)
deliver(truckB)

class Main:
    print("Western Governors University Parcel Service (WGUPS)")
    print("Route total mileage: ")
    print(truckA.miles + truckB.miles + truckC.miles)
    user_input = input("To see package info, please type 'go', otherwise any other command"
    " will exit program")
    if user_input == "go":
        try:
            user_entry = input("To check status of package, please enter time using the HH:MM:SS format")
            (hours, mins, secs) = user_entry.split(":")
            change_time = datetime.timedelta(hours = int(hours), minutes = int(mins), seconds = int(secs))
            next_input = input("If you would like to see the status of a single package, please type 'single'."
            " To see the status of all packages, please type 'all'.")
            if next_input == "single":
                try:
                    single_pack = input("Enter package ID number")
                    package = pack_hash_table.find(int(single_pack))
                    package.status_report(change_time) 
                    print(str(package)) 
                except ValueError:
                    print("Invalid entry. Closing program.")
                    exit()
            elif next_input == "all":
                try:
                    print("ID      Address       City     Zip     Weight      Due      Status      Departure      Delivery")
                    for package_id in range(1, 41):
                        package = pack_hash_table.find(package_id)
                        package.status_report(change_time)
                        print(str(package))
                except ValueError:
                    print("Invalid entry. Closing program.")
                    exit()
            else:
                exit()
        except ValueError:
            print("Invalid entry. Closing program.")
            exit()
    elif user_input != "go":
        print("Invalid entry. Closing program.")
        exit()
