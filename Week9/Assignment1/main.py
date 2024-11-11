# Create an application for a car park that has paid parking. The main functionality of this terminal application is to register incoming and departing cars (check-in and check-out) from a car park while it keeps track of the current capacity and calculates the owed parking fee when a car leaves the car park.
#
# The classes that need to be programmed for this assignment are described below.
#
# Class CarParkingMachine:
# Attributes/Fields:
# capacity (int, default 10) - how many cars can be parked at the car park at the same time.
# hourly_rate (float, default 2.50) - used to calculate the parking fee.
# parked_cars (dict => key: license_plate, value: ParkedCar object) - keeps track of which cars are currently in the car park
# Methods:
# init (constructor) that receives the capacity, hourly_rate and sets the parked_cars dict as empty.
# check_in that receives the license_plate as str, the check_in as datetime object that the car is parked (optional, default = current time).
# If the maximum capacity is reached it should return False and not check-in the car.
# check_out that receives the license_plate as str and returns the owed parking fee total
# (by calling the get_parking_fee method).
# should return a decimal number (float)
# get_parking_fee that receives the license_plate as str and calculates/returns the parking fee
# (hourly_rate * whole parking hours rounded-up, with max of 24 hours).
#
# Class ParkedCar:
# Attributes/Fields:
# license_plate (str) - license plate of the car
# check_in (datetime) - datetime object of the time checked-in
# Methods:
# init (constructor) that receives the license_plate and check-in
#
# Extra:
# Additional research is required on how to handle datetime objects to calculate the difference between the check-in and check-out time and how to round-up in hours. Hint: import the datetime module (datetime and timedelta objects)
#
# In order to test your class, use the provided unit test file and complete the test functions with your own code.
#
# Default menu:
# [I] Check-in car by license plate
# [O] Check-out car by license plate
# [Q] Quit program
#
# Input example (check-in):
# I
# License: AA-123-B
# Q
# Output example (check-in - OK):
# License registered
#
# Output example (check-in - Capacity reached):
# Capacity reached!
#
#
# Input example (check-out):
# I
# License: AA-123-B
# O
# License: AA-123-B
# Q
# Output example (check-out - OK):
# Parking fee: 2.50 EUR
#
# Output example (check-out - Not found):
# License AA-321-B not found!
import math
from datetime import datetime


class CarParkingMachine:
    """
    Car parking machine
    Used to track parked cars and calculate fees
    """

    def __init__(self, capacity=10, hourly_rate=2.50):
        """
        Instantiates a new car parking
        :param capacity: The maximum capacity of the car park, defaults to 10
        :param hourly_rate: The hourly rate of the car park, defaults to 2.50
        """
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = dict()

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


MENU_OPTIONS = """[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program
"""


def main():
    """
    The main program
    :return:
    """
    car_parking = CarParkingMachine()

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
