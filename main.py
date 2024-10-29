# Dominique Brown-Gonzalez, Student ID 001005137

import datetime

import hashtable
from package import pkgs_to_hash_table
from truck import get_address, get_distance, truck_one, truck_two, truck_three

# Create hash table object
# O(1) space-time complexity
ht = hashtable.HashTable()

# Call get_pkg_data to insert csv data into hash table
pkgs_to_hash_table("csv_files/WGUPS_Packages_Table.csv", ht)


# Method to order packages on truck, determine the shortest route using the Nearest Neighbor algorithm,
# and update truck and package data
def deliver(truck_obj):
    # Empty list to hold all packages yet to be delivered
    # O(1) space-time complexity
    to_be_delivered = []

    # O(n^2) time complexity for this for loop with 2 method calls: O(n) * O(n) + O(1)
    # O(n) space complexity...O(n)+O(n)+O(1) = O(2n+1) = O(n)
    for package_ID in truck_obj.pkgs:  # O(n)
        pk = ht.lookup(package_ID)  # O(n)
        to_be_delivered.append(pk)  # O(1)

    # clear chosen truck's list for reorganization of packages in nearest neighbor order
    # O(n) runtime complexity
    truck_obj.pkgs.clear()

    # Loop through to_be_delivered list using Nearest Neighbor until there are no remaining deliverable packages
    # O(n^2) time complexity
    # O(n) space complexity...O(n)+O(1)+O(1)+O(n)+O(1)+O(1)+O(1) = O(2n+5) = O(n)
    while len(to_be_delivered) > 0:  # O(n)
        next_stop = 3000  # arbitrarily large number, O(1)
        next_pkg = None  # O(1)
        for pk in to_be_delivered:  # O(n)
            if get_distance(get_address(truck_obj.starting_address), get_address(pk.address)) <= next_stop:  # O(1)
                next_stop = get_distance(get_address(truck_obj.starting_address), get_address(pk.address))  # O(1)
                next_pkg = pk  # O(1)

        # Append nearest neighbor package to truck's deliverable package list
        # Amortized O(1) space-time complexity
        truck_obj.pkgs.append(next_pkg.pkg_id)

        # Remove package added in previous line from to_be_delivered list
        # O(n) time complexity
        # O(1) space complexity
        to_be_delivered.remove(next_pkg)

        # Truck's mileage is updated
        # O(1) space-time complexity
        truck_obj.mileage += next_stop

        # Truck's starting address is updated
        # O(1) space-time complexity
        truck_obj.starting_address = next_pkg.address

        # Truck's travel time to the nearest next stop is updated
        # O(1) space-time complexity
        truck_obj.time += datetime.timedelta(hours=next_stop / truck_obj.mph)

        # Package's delivery time is updated
        # O(1) space-time complexity
        next_pkg.delivered_at = truck_obj.time

        # Package's departure time from current stop is updated
        # O(1) space-time complexity
        next_pkg.depart = truck_obj.depart


# Call the 'deliver' function to load/order packages on trucks
deliver(truck_one)
deliver(truck_two)
deliver(truck_three)

# variable to hold value of total mileage of all three delivery trucks
total_mileage = str(truck_one.mileage + truck_two.mileage + truck_three.mileage)  # O(1) space-time complexity


# Main class
class Main:
    # CLI
    # User will see the next visible 23 lines as a message/introduction to the interface
    print("\n")
    print("\n")
    print("\n**** Western Governors University Parcel Service ****")
    print("\n ********** WGUPS Package Tracking System **********\n")
    print("\n")
    # Total mileage of all trucks, packages on each truck, and total mileage of individual trucks displayed
    print("Total mileage for all trucks/deliveries: " + total_mileage + " miles\n")
    print("Packages on Truck 1, in order of delivery: " + str(truck_one.pkgs))
    print("Truck 1's departure time: " + str(truck_one.depart) + ", Truck 1's finishing time: " + str(truck_one.time))
    print("Truck 1's mileage: " + str(round(truck_one.mileage, 1)) + " miles\n")
    print("Packages on Truck 2, in order of delivery: " + str(truck_two.pkgs))
    print("Truck 2's departure time: " + str(truck_two.depart) + ", Truck 2's finishing time: " + str(truck_two.time))
    print("Truck 2's mileage: " + str(round(truck_two.mileage, 1)) + " miles\n")
    print("Packages on Truck 3, in order of delivery: " + str(truck_three.pkgs))
    print("Truck 3's departure time: " + str(truck_three.depart) + ", Truck 3's finishing time: " +
          str(truck_three.time))
    print("Truck 3's mileage: " + str(round(truck_three.mileage, 1)) + " miles\n")
    print("\n")
    # Options menu is displayed
    print("*****      Options      *****\n")
    print("\n")
    print("You will first be asked for a time linked to the package(s) status, then...")
    print("1) Enter 'all' to view a list of all packages and their locations\n")
    print("2) Enter 'package' to select a specific package and its location at a specific time\n")
    print("3) Enter 'exit' to exit the program\n")
    # User is asked to input a time
    time_input = input("Please enter a time in HH:MM:SS format to continue checking the status of a package "
                       "or packages: ")
    (h, m, s) = time_input.split(":")
    to_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    headers = "Columns below are listed in this order:\n" \
              "Package ID, Address, City, State, Zip Code, Deadline, Weight, Special Notes, Package Status, " \
              "Departure Time, Expected Delivery Time/Time Delivered\n"

    # User is asked to type in their option preference
    # Program will exit upon input of "exit" or invalid input
    start = input("Please type 'all' or 'package' to continue, or type 'exit' to exit the program.\n")
    if start == "package":
        try:
            # User asked for a package id in order to search for and display an individual package
            # Anything other than a valid package id will cause the program to exit
            single_pkg = input("Please enter the package ID (integers only): ")
            pk = ht.lookup(int(single_pkg))  # O(n)
            pk.package_status(to_timedelta)  # O(1)
            print("\n")
            print(headers)
            print(str(pk))
        except ValueError:
            print("Invalid entry. Exiting program.")
            exit()
    # Displays all package data for input time
    elif start == "all":
        try:
            print(headers)
            for package_id in range(1, 41):  # O(n)
                pk = ht.lookup(package_id)  # O(n)
                pk.address_correct(to_timedelta)  # O(1)
                pk.package_status(to_timedelta)  # O(n)
                print("\n")
                print(str(pk))
        except ValueError:
            print("Invalid entry. Exiting program.")
            exit()

    elif start == "exit":
        print("Exit chosen. Exiting program.")
        exit()
    elif start != ("all" or "package" or "exit"):
        print("Invalid entry. Exiting program.")
    else:
        exit()
