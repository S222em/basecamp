def average_speed(distance_in_km: float, time_in_hours: float) -> str:
    """
    Calculates the average speed
    :param distance_in_km:
    :param time_in_hours:
    :return: String with rounded average speed and km/h
    """
    if time_in_hours == 0:
        return "---"

    average = distance_in_km / time_in_hours

    return f"{round(average, 1 if abs(average) < 10.0 else None)} km/h"


def main():
    distance_in_km = float(input("Distance in km: "))
    time_in_hours = float(input("Time in hours: "))

    print(average_speed(distance_in_km, time_in_hours))


if __name__ == "__main__":
    main()
