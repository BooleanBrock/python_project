import datetime
from builtins import ValueError
from algorithm import *

#Command Line Interface for user
class Main:
    print("Western Governors University Parcel Service (WGUPS)")
    
    #Display total miles required to deliver all packages
    print("Route total mileage: ")
    print(truckA.miles + truckB.miles + truckC.miles)

    #Prompt user to start program by inputting "go". If user wishes to exit, any other command will exit program
    user_input = input("To see package info, please type 'go', otherwise any other command"
    " will exit program")
    if user_input == "go":
        try:

            #Prompt user to enter time they would wish to check status of package
            #Convert user entry to time
            user_entry = input("To check status of package, please enter time using the HH:MM:SS format")
            (hours, mins, secs) = user_entry.split(":")
            change_time = datetime.timedelta(hours = int(hours), minutes = int(mins), seconds = int(secs))

            #Prompt user to specify if they would like to view one or all packages
            next_input = input("If you would like to see the status of a single package, please type 'single'."
            " To see the status of all packages, please type 'all'.")

            #User must enter "single" to see one package
            if next_input == "single":
                try:
                    #User must enter ID number of package they would like to view. Invalid entries will exit the program.
                    single_pack = input("Enter package ID number")
                    package = pack_hash_table.find(int(single_pack))
                    package.status_report(change_time) 
                     #Provides header to understand data being provided
                    print("ID      Address       City     Zip     Weight      Due      Status      Departure      Delivery")
                    print(str(package)) 
                except ValueError:
                    print("Invalid entry. Closing program.")
                    exit()
            
            #If user types "all", they will see data for all packages
            elif next_input == "all":
                try:
                    #Provides header to understand data being provided
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
