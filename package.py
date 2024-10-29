import csv
import datetime


# Package class
class Package(object):
    # Constructor with attributes equivalent to package csv fields
    # O(1) space-time complexity
    def __init__(self, pkg_id, address, city, state, zip_code, deadline, weight, special_notes, status):
        self.pkg_id = pkg_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.depart = None
        self.delivered_at = None

    # Method to return attributes as string
    # O(1) space_time complexity
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (self.pkg_id, self.address, self.city, self.state,
                                                                 self.zip_code, self.deadline, self.weight,
                                                                 self.special_notes,
                                                                 self.status, self.depart, self.delivered_at)

    # Method to update status of package from 'At Hub' to 'En Route' to 'Delivered'
    # O(1) space-time complexity
    def package_status(self, to_timedelta):
        # Mark "Delivered" if delivered_at is before the input time
        if self.delivered_at < to_timedelta:
            self.status = "Delivered"
        # Mark as "En Route" if depart is before or equal to input time and delivered_at is after input time
        elif self.depart <= to_timedelta < self.delivered_at:
            self.status = "En Route"
        # Otherwise, mark as "At Hub"
        else:
            self.status = "At Hub"

    # Method to correct package 9's address at 10:20:00
    # O(1) space-time complexity
    def address_correct(self, to_timedelta):
        to_timedelta2 = datetime.timedelta(hours=int("10"), minutes=int("20"), seconds=int("00"))
        if to_timedelta >= to_timedelta2:
            if self.pkg_id == 9:
                self.address = "410 S State St"
                self.zip_code = "84111"


# Read csv files for packages, distances and addresses
with open("csv_files/WGUPS_Packages_Table.csv") as csv_pkgs:
    pkgs_csv = csv.reader(csv_pkgs)
    pkgs_CSV = list(pkgs_csv)


# Create package objects using csv data and insert into hash table
# O(n^2) time complexity
# O(n) space complexity
def pkgs_to_hash_table(filename, h):
    with open(filename) as p_data:
        pkg_data = csv.reader(p_data)
        for p in pkg_data:  # O(n)
            package_id = int(p[0])
            package_address = p[1]
            package_city = p[2]
            package_state = p[3]
            package_zip_code = p[4]
            package_deadline = p[5]
            package_weight = p[6]
            package_notes = p[7]
            package_status = "At Hub"

            _pkg = Package(package_id, package_address, package_city, package_state, package_zip_code, package_deadline,
                           package_weight, package_notes, package_status)  # O(1)

            # Insert package data using package_id as key and _pkg as value
            # O(n)
            h.insert(package_id, _pkg)
