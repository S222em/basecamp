# Our car parking machine from the previous assignment is a success. But to roll our system to more parking garages in the city we need some changes and improvements that are not yet in the current system.
#
# When the system restarts for whatever reason we want to continue with the already parked cars.
# We want to keep track of all the parking actions in a central system and want to know in which parking garage the action has happened.
# For this assignment you are going to expand your carparking program to handle file reading and writing.
#
# Two new additions need to be added to the existing program from week 09 which will be explained in depth below.
#
# Extend Class CarParkingMachine:
# Attributes/Fields:
# id (string) - to identify this machine.
# Extra:
# When initializing a car parking machine you should load all non checked-out cars (checked-in but not checked-out) from the log file for this specific machine (example 'North'). Be sure to not check-in these cars again (as this will create new log lines), but only load them in the car parking machine instance/object.
#
#
# Class CarParkingLogger:
# Info:
# Create a new class named CarParkingLogger which contains (at least) a method to log a car check-in and a method to log a car check-out. The class should use an id to identify for which parking machine this logger is.
# Every check-in and check-out should write a line to a logfile named 'carparklog.txt' which is shared by all car parking machines. The lines should be written in a specific format as shown in the following examples:
#
# Attributes/Fields:
# id (string) - to identify this machine.
# Methods:
# get_machine_fee_by_day that receives the car_parking_machine_id as str (case-insensitive) and a search_date as str with format (DD-MM-YYYY). It should return the total parking fee for a specific car parking machine on a specific day rounded up to two decimals.
# get_total_car_fee that receives the license_plate as str and returns the total fee independent of the car parking machine used and should be rounded up to two decimals
# Examples:
# Car parking machine North with a parking fee rate of 2 euro per hour checks in a car with license_plate SG-123-B on February 9 at 14:33:54 (hours, minutes, seconds)
#
# This should result in the following log line:
# 09-02-2022 14:33:54;cpm_name=North;license_plate=SG-123-B;action=check-in
#
# Car parking machine North checks the same car out at 16:50:02
#
# This should result in the following log line:
# 09-02-2022 16:50:02;cpm_name=North;license_plate=SG-123-B;action=check-out;parking_fee=6
#
# Extra:
# Hint: use the datetime module to modify your datetime to the correct format.
#
# To test your code, use the test file from the assignment of week 09. Make sure to use os.getcwd() to get the current absolute directory sys.path[0] will not work

import math
from datetime import datetime

LOG_FILE = "carparklog.txt"
TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M:%S"


class CarParkingMachine:
    """
    Car parking machine
    Used to track parked cars and calculate fees
    """

    def __init__(self, id, capacity=10, hourly_rate=2.50, log=True):
        """
        Instantiates a new car parking
        :param id: The ID of this carpark
        :param capacity: The maximum capacity of the car park, defaults to 10
        :param hourly_rate: The hourly rate of the car park, defaults to 2.50
        :param log: Whether the carpark should use the log
        """
        self.id = id.lower()
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = dict()

        if log:
            self._load()
            self.logger = CarParkingLogger(self.id)

    def _load(self):
        """
        Loads all previous parked cars from the log file
        :return:
        """
        cars = dict()

        # Gather all the cars still in the park
        with open(LOG_FILE) as file:
            for line in file.readlines():
                if self.id not in line:
                    continue

                line_contents = line.split(";")
                license_plate = line_contents[2][14:]

                if "check-in" in line:
                    time = datetime.strptime(line_contents[0], TIMESTAMP_FORMAT)
                    cars[license_plate] = time
                if "check-out" in line:
                    del cars[license_plate]

        # Load the still parked cars back into this carpark
        for license_plate, check_in in cars.items():
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)

    def check_in(self, license_plate, check_in=datetime.now()):
        """
        Checks a car in if there is space left in the car park
        :param license_plate: The license plate of the to check in car
        :param check_in: The time the car was checked in, defaults to now
        :return:
        """
        if len(self.parked_cars) >= self.capacity:
            return False

        parked_car = ParkedCar(license_plate, check_in)
        self.parked_cars[license_plate] = parked_car

        if hasattr(self, "logger"):
            self.logger.check_in(license_plate, check_in)

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
                if id.lower() not in line or date not in line or 'check-out' not in line:
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
