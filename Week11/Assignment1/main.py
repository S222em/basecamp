# Request:
# Projects always have room for improvement. Luckily we have learned this week about CSV and JSON. Things the owner wants to have solved.
#
# Car parking machines should technically be more separated.
# People could successfully check-in in multiple garages at the same time.
# There was no easy way to get details about a specific garage.
# The code to recover the garage state was getting slow overtime and a bit complicated.
# New add JSON CSV:
# For this assignment you are going to expand your carparking program to handle reading and writing of structured data files in JSON and CSV format. New functionality needs to be added to the existing program from week 10 which will be explained in depth below.
#
# Retrieving and storing the car parking machine state with a JSON data file:
# In the previous assignment you created functionality to load the state (parked cars) of car parking machines from the log files. Now you will modify this functionality by using a JSON data file to read/write the state of the car parking machines.
#
# Every car parking machine will save the state in its own JSON file! Provide a unique name or ID when instantiating a new car parking machine object. Use this name (or ID) to create a JSON file with this name (or ID), for example "parking-machine-north-001.json". If the JSON file already exists (for example this specific car parking machine object has been created earlier) the exisitng file should be used and the previous state should be read and loaded.
#
# The state should contain the parked cars from the car parking machine. See the following JSON format to store parked cars in the file:
#
# [
#     {
#         "license_plate": "2-ABC-09",
#         "check_in": "09-21-2022 16:20:04"
#     },
#     {
#         "license_plate": "3-XYZ-10",
#         "check_in": "09-21-2022 17:20:50"
#     }
# ]
# The following actions will result in data being read from or written to the JSON data file:
#
# Check-in of a car (add car to json)
# Check-out of a car (remove car from json)
# Check-in validation:
# A car should only be able to check-in at a car parking machine it does not have an open check-in (checked-in, but not checked-out yet) at another car parking machine within the same timeframe. Modify the CarParkingMachine class check_in method to add this new functionality.
#
# To be able to check all currently parked cars in all car parking machines, you should keep track of created car parking machine instances and check their car parking machine states. A possible solution would be to create a list in your main program and add the name (or ID) of created parking machine to that list. The check-in method of a car parking machine could use that list to know which JSON state files to check.
#
# Reporting program:
# Create a program (carparkingreports.py) with the following menu structure:
#
# [P] Report all parked cars during a parking period for a specific parking machine input: car parking machine identifier, from date, to date (date format: DD-MM-YYYY). Input is comma seperated. output: csv file example (semicolon seperated):
#
# license_plate;check-in;check-out;parking_fee
# 2-ABC-09;09-21-2022 16:20:04;09-21-2022 17:20:30;5.00
# 3-XYZ-10;09-21-2022 12:20:04;09-21-2022 18:45:11;18.00
# [F] Report total collected parking fee during a parking period for all parking machines input: from date, to date (date format: DD-MM-YYYY) Input is comma seperated. output: csv file example (semicolon seperated):
#
# car_parking_machine;total_parking_fee
# cpm_north;2,050
# cpm_south;180
# [Q] Quit program
#
# The information for the reports is based on the information in the log file.
import json
import math
import os.path
import weakref
from datetime import datetime

LOG_FILE = "carparklog.txt"
TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M:%S"


class CarParkingMachine:
    """
    Car parking machine
    Used to track parked cars and calculate fees
    """

    # Contains all instances to confirm whether a car is already parked somewhere else.
    # To make sure instances will not stay alive because of a reference here, WeakSet is used.
    INSTANCES = weakref.WeakSet()

    def __init__(self, id, capacity=10, hourly_rate=2.50, log=True):
        """
        Instantiates a new car parking
        :param id: The ID of this carpark
        :param capacity: The maximum capacity of the car park, defaults to 10
        :param hourly_rate: The hourly rate of the car park, defaults to 2.50
        :param log: Whether the carpark should use the log
        """
        self.id = id
        self._json_file = f"{id}_state.json"
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = dict()

        if log:
            self._load()
            self.logger = CarParkingLogger(id)

        CarParkingMachine.INSTANCES.add(self)

    def _load(self):
        """
        Loads all previous parked cars from json file if present
        :return:
        """
        if not os.path.exists(self._json_file):
            return

        # Load the cars still in the park
        with open(self._json_file) as file:
            cars = json.load(file)

        # Load the still parked cars back into this carpark
        for car in cars:
            parked_car = ParkedCar.from_json(car)
            self.parked_cars[parked_car.license_plate] = parked_car

    def _save(self):
        """
        Saves the current state to this carparks json_file
        :return:
        """
        with open(self._json_file, "w") as file:
            json.dump(list((car.to_json() for car in self.parked_cars.values())), file)

    @staticmethod
    def is_car_checked_in(license_plate):
        """
        Whether the car is checked in on any instance
        :param license_plate:
        :return:
        """
        for instance in CarParkingMachine.INSTANCES:
            if license_plate in instance.parked_cars:
                return True

        return False

    def check_in(self, license_plate, check_in=datetime.now()):
        """
        Checks a car in if there is space left in the car park
        :param license_plate: The license plate of the to check in car
        :param check_in: The time the car was checked in, defaults to now
        :return:
        """
        if len(self.parked_cars) >= self.capacity or self.is_car_checked_in(license_plate):
            return False

        parked_car = ParkedCar(license_plate, check_in)
        self.parked_cars[license_plate] = parked_car

        if hasattr(self, "logger"):
            self.logger.check_in(license_plate, check_in)

        self._save()

        return True

    def check_out(self, license_plate):
        """
        Check the car out of the park if it was there in the first place
        :param license_plate: The license plate of the car to check out
        :return:
        """
        if license_plate not in self.parked_cars:
            return None

        fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)

        if hasattr(self, "logger"):
            self.logger.check_out(license_plate, fee)

        self._save()

        return fee

    def get_parking_fee(self, license_plate):
        """
        Returns the fee of a car in the park
        :param license_plate:
        :return:
        """
        return self.hourly_rate * self.parked_cars[license_plate].get_hours_since_check_in()


class ParkedCar:
    """
    A car parked in the car park
    """

    def __init__(self, license_plate, check_in):
        """
        Instantiates a new parked car
        :param license_plate: The license plate of the car
        :param check_in: The time the car was checked in
        """
        self.license_plate = license_plate
        self.check_in = check_in

    def get_hours_since_check_in(self):
        """
        Returns the hours since the car was checked in
        Maximum is 24 hours
        :return:
        """
        return min(math.ceil((datetime.now() - self.check_in).total_seconds() / 3600), 24)

    @staticmethod
    def from_json(data):
        check_in = datetime.strptime(data["check_in"], TIMESTAMP_FORMAT)
        return ParkedCar(data["license_plate"], check_in)

    def to_json(self):
        return {
            "license_plate": self.license_plate,
            "check_in": self.check_in.strftime(TIMESTAMP_FORMAT)
        }


class CarParkingLogger:
    """
    Used to log actions from a carparkingmachine to the log file
    """

    def __init__(self, id):
        """
        Creates a new logger
        :param id: The ID of the car parking this belongs too
        """
        self.id = id

    def _log(self, content, now=datetime.now()):
        """
        Create and write a new message with timestamp and car parking id
        :param content:
        :return:
        """
        line = f"{now.strftime(TIMESTAMP_FORMAT)};cpm_name={self.id};{content}\n"
        with open(LOG_FILE, "a") as file:
            file.write(line)

    def check_in(self, license_plate, now):
        """
        Logs a check in
        :param license_plate: The license plate of the checked in car
        :param now: The current time
        :return:
        """
        line = f"license_plate={license_plate};action=check-in"
        self._log(line, now)

    def check_out(self, license_plate, fee):
        """
        Logs a check-out
        :param license_plate: The license plate of the checkout car
        :param fee: Parking fee
        :return:
        """
        line = f"license_plate={license_plate};action=check-out;parking_fee={fee}"
        self._log(line)

    @staticmethod
    def get_machine_fee_by_day(id, date):
        """
        Returns the total collected fee for a car park on a certain date
        :param id: ID of the carpark
        :param date: DD-MM-YYYY
        :return:
        """
        total_fee = 0.0

        with open(LOG_FILE) as file:
            for line in file.readlines():
                if id not in line or date not in line or 'check-out' not in line:
                    continue

                line_contents = line.split(";")
                total_fee += float(line_contents[4][12:])

        return round(total_fee, 2)

    @staticmethod
    def get_total_car_fee(license_plate):
        """
        Returns the total fees for a single car
        :param license_plate: The license plate of the car
        :return:
        """
        total_fee = 0.0

        with open(LOG_FILE) as file:
            for line in file.readlines():
                if license_plate not in line or 'check-out' not in line:
                    continue

                line_contents = line.split(";")
                total_fee += float(line_contents[4][12:])

        return round(total_fee, 2)


MENU_OPTIONS = """[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program
"""


def main():
    """
    The main program
    :return:
    """

    car_parking = CarParkingMachine("Main")

    while True:
        stop = loop(car_parking)
        if stop:
            break


def loop(car_parking):
    """
    The main loop
    :param car_parking:
    :return: Whether the program should quit
    """
    menu_option = input(MENU_OPTIONS).strip().lower()

    if menu_option == "q":
        return True

    license_plate = input("License: ")

    if menu_option == "i":
        is_checked_in = car_parking.check_in(license_plate)
        print("License registered" if is_checked_in else "Capacity reached!")

    if menu_option == "o":
        parking_fee = car_parking.check_out(license_plate)

        if not parking_fee:
            print(f"License {license_plate} not found!")
        else:
            print(f"Parking fee: {parking_fee:.2f} EUR")

    return False


if __name__ == "__main__":
    main()
