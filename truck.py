import csv
import datetime


# Truck class
class Truck:
    # Constructor with truck attributes
    # O(1)
    def __init__(self, num_pkgs, mph, load_pkg, pkgs, mileage, starting_address, depart):
        self.num_pkgs = num_pkgs
        self.mph = mph
        self.load_pkg = load_pkg
        self.pkgs = pkgs
        self.mileage = mileage
        self.starting_address = starting_address
        self.depart = depart
        self.time = depart

    # Method to return package attributes as string
    # O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.num_pkgs, self.mph, self.load_pkg, self.pkgs, self.mileage,
                                               self.starting_address, self.depart)


# Read csv files for distances and addresses
with open("csv_files/WGUPS_Distances_Table.csv") as csv_dists:
    dists_csv = csv.reader(csv_dists)
    dists_CSV = list(dists_csv)

with open("csv_files/WGUPS_Addresses_Table.csv") as csv_addresses:
    addresses_csv = csv.reader(csv_addresses)
    addresses_CSV = list(addresses_csv)

    # Method to return address id
    # O(n)
    def get_address(address):
        for row in addresses_CSV:  # O(n)
            if address in row[2]:  # O(1)
                return int(row[0])  # O(1)

    # Method to get distance between address x and address y (current address and next)
    # O(1)
    def get_distance(x, y):
        distance = dists_CSV[x][y]
        if distance == '':
            distance = dists_CSV[y][x]
        return float(distance)


# variable to hold truck capacity value
truck_capacity = 16

# variable to hold truck average speed value
truck_speed = 18

# Manually load trucks
truck_one_pkgs = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck_two_pkgs = [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
truck_three_pkgs = [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33]

# variable to hold truck mileage, initialized to 0.0
truck_mileage = 0.0

# variable that maps to starting_address
hub = "4001 South 700 East"

# truck departure times
leave_hub_one = datetime.timedelta(hours=8, minutes=0)
leave_hub_two = datetime.timedelta(hours=9, minutes=10)
leave_hub_three = datetime.timedelta(hours=11, minutes=00)

# truck objects
truck_one = Truck(truck_capacity, truck_speed, None, truck_one_pkgs, truck_mileage, hub, leave_hub_one)
truck_two = Truck(truck_capacity, truck_speed, None, truck_two_pkgs, truck_mileage, hub, leave_hub_two)
truck_three = Truck(truck_capacity, truck_speed, None, truck_three_pkgs, truck_mileage, hub, leave_hub_three)


