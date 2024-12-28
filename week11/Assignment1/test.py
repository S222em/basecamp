import os
from datetime import datetime, timedelta
from random import randint

from Assignment1.main import CarParkingMachine


# Can be used to clear the log
def _clear():
    directory = os.path.dirname(__file__)
    for file in os.listdir(directory):
        if not file.endswith(".json") and not file.endswith(".txt"):
            continue

        os.remove(os.path.join(directory, file))


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    car_park = CarParkingMachine("Test1", log=False)
    assert car_park.check_in("test-license-1-1") == True

    _clear()


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    car_park = CarParkingMachine("Test2", capacity=1, log=False)
    car_park.check_in("test-license-2-1")
    assert car_park.check_in("test-license-2-2") == False

    _clear()


# Test for checking the correct parking fees
def test_parking_fee():
    car_park = CarParkingMachine("Test3", log=False)

    # Assert that parking time 2h10m, gives correct parking fee
    car_park.check_in("test-license-3-1", datetime.now() - timedelta(hours=2, minutes=10))
    assert car_park.get_parking_fee("test-license-3-1") == 7.5

    # Assert that parking time 24h, gives correct parking fee
    car_park.check_in("test-license-3-2", datetime.now() - timedelta(hours=24))
    assert car_park.get_parking_fee("test-license-3-2") == 60

    # Assert that parking time 30h == 24h max, gives correct parking fee
    car_park.check_in("test-license-3-3", datetime.now() - timedelta(hours=30))
    assert car_park.get_parking_fee("test-license-3-3") == 60

    _clear()


# Test for validating check-out behaviour
def test_check_out():
    car_park = CarParkingMachine("Test4", log=False)

    car_park.check_in("test-license-4-1")

    # Assert that {license_plate} is in parked_cars
    assert "test-license-4-1" in car_park.parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    assert car_park.check_out("test-license-4-1") == 2.5
    # Assert that {license_plate} is no longer in parked_cars
    assert "test-license-4-1" not in car_park.parked_cars

    _clear()


# Test whether the car park is restored from the json file
def test_restore():
    # Create a new carpark with id test
    first_car_park = CarParkingMachine("Test5")
    # Park a car
    first_car_park.check_in("test-license-5-1")

    # Create a second carpark with id test
    # This should load the parked car from the first instance
    second_car_park = CarParkingMachine("Test5")
    assert second_car_park.check_out("test-license-5-1") is not None

    _clear()


def test_get_machine_fee_by_day():
    now = datetime.now()
    cpm_name = str('CodeGradeTestCPNSouth' + str(randint(1, 1000000000000000000)))
    cpm_south = CarParkingMachine(id=cpm_name, hourly_rate=1.55)

    cpm_south.check_in(license_plate='KKK', check_in=now - timedelta(hours=30))
    cpm_south.check_out(license_plate='KKK')
    cpm_south.check_in(license_plate='KKK')
    cpm_south.check_out(license_plate='KKK')
    cpm_south.check_in(license_plate='JJJ')
    cpm_south.check_out(license_plate='JJJ')
    cpm_south.check_in(license_plate='LLL')
    cpm_south.check_out(license_plate='LLL')
    cpm_south.check_in(license_plate='MMM')

    total_car_fee = cpm_south.logger.get_machine_fee_by_day(cpm_name, now.strftime('%d-%m-%Y'))
    assert 41.85 == float(total_car_fee), "Validate correct total car fee amount (41.85)"
    _clear()
