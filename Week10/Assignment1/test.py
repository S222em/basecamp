from datetime import datetime, timedelta
from random import randint

from Assignment1.main import CarParkingMachine, LOG_FILE


# Can be used to clear the log
def _clear_log():
    open(LOG_FILE, "w").close()


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    car_park = CarParkingMachine("Test", log=False)
    assert car_park.check_in("test-license-1") == True


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    car_park = CarParkingMachine("Test", capacity=1, log=False)
    car_park.check_in("test-license-1")
    assert car_park.check_in("test-license-2") == False


# Test for checking the correct parking fees
def test_parking_fee():
    car_park = CarParkingMachine("Test", log=False)

    # Assert that parking time 2h10m, gives correct parking fee
    car_park.check_in("test-license-1", datetime.now() - timedelta(hours=2, minutes=10))
    assert car_park.get_parking_fee("test-license-1") == 7.5

    # Assert that parking time 24h, gives correct parking fee
    car_park.check_in("test-license-2", datetime.now() - timedelta(hours=24))
    assert car_park.get_parking_fee("test-license-2") == 60

    # Assert that parking time 30h == 24h max, gives correct parking fee
    car_park.check_in("test-license-3", datetime.now() - timedelta(hours=30))
    assert car_park.get_parking_fee("test-license-3") == 60


# Test for validating check-out behaviour
def test_check_out():
    car_park = CarParkingMachine("Test", log=False)

    car_park.check_in("test-license-1")

    # Assert that {license_plate} is in parked_cars
    assert "test-license-1" in car_park.parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    assert car_park.check_out("test-license-1") == 2.5
    # Assert that {license_plate} is no longer in parked_cars
    assert "test-license-1" not in car_park.parked_cars


# Test whether the car park can read and write data from the log file
def test_log():
    # Create a new carpark with id test
    first_car_park = CarParkingMachine("Test")
    # Park a car
    first_car_park.check_in("test")

    # Create a second carpark with id test
    # This should load the parked car from the first instance
    second_car_park = CarParkingMachine("Test")
    assert second_car_park.check_out("test") is not None

    _clear_log()


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
    _clear_log()
