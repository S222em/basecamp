from main import average_speed


def test_average_speed_1():
    assert "50 km/h" == average_speed(100.0, 2.0)


def test_average_speed_2():
    assert "33 km/h" == average_speed(100.0, 3.0)


def test_average_speed_3():
    assert "---" == average_speed(100.0, 0)


def test_average_speed_4():
    assert "5.0 km/h" == average_speed(10.0, 2)
