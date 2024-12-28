from datetime import datetime, timedelta

from Assignment1.main import CarParkingMachine


# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    car_park = CarParkingMachine()
    assert car_park.check_in("test-license-1") == True


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    car_park = CarParkingMachine(capacity=1)
    car_park.check_in("test-license-1")
    assert car_park.check_in("test-license-2") == False


# Test for checking the correct parking fees
def test_parking_fee():
    car_park = CarParkingMachine()

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
    car_park = CarParkingMachine()

    car_park.check_in("test-license-1")

    # Assert that {license_plate} is in parked_cars
    assert "test-license-1" in car_park.parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    assert car_park.check_out("test-license-1") == 2.5
    # Assert that {license_plate} is no longer in parked_cars
    assert "test-license-1" not in car_park.parked_cars
