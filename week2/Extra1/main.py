import math
import re
from datetime import timedelta, datetime

SHAPE_PATTERN = re.compile("(rectangle|circle)")
DISTANCE_PATTERN = re.compile("(\d+|\d+\.\d+)(m|cm|mm)")
# 0.66m3/hour (rounded)
AVERAGE_VOLUME_PER_SECOND = 190000


def main():
    shape = get_shape_until_valid()

    volume = get_cuboid_volume() if shape == "rectangle" else get_cylinder_volume()

    time_in_seconds = volume // AVERAGE_VOLUME_PER_SECOND

    time = timedelta(seconds=time_in_seconds)
    finished = datetime.now() + time

    print(
        f"It takes an average of {f'{time.days} days, ' if time.days != 0 else ''}{f'{time.seconds // 3600} hours and ' if time.seconds // 3600 != 0 else ''}{round_minute_to_quarter(time.seconds % 3600 // 60):02d} minutes to fill your pool")
    print(
        f"Your pool will be full around {finished.day:02d}-{finished.month:02d}-{finished.year} at {finished.hour:02d}:{round_minute_to_quarter(finished.minute):02d}")


def get_cuboid_volume() -> float:
    width = get_distance_until_valid("Width")
    depth = get_distance_until_valid("Depth")
    length = get_distance_until_valid("Length")

    return width * depth * length


def get_cylinder_volume() -> float:
    diameter = get_distance_until_valid("Diameter")
    depth = get_distance_until_valid("Depth")

    return math.pi * pow(diameter / 2, 2) * depth


def round_minute_to_quarter(minute: int) -> int:
    return min(45, max(1, math.ceil(minute / 15)) * 15)


def get_shape_until_valid() -> str:
    while True:
        shape = input("Shape of the pool (rectangle/circle): ").strip().lower()
        if SHAPE_PATTERN.fullmatch(shape) is not None:
            return shape

        print("Please enter the shape of your pool: rectangle or circle")


def get_distance_until_valid(prompt: str) -> float:
    while True:
        distance = input(f"{prompt} (mm/cm/m): ").strip()
        if DISTANCE_PATTERN.fullmatch(distance) is not None:
            return parse_distance(distance)

        print(
            "Please use the correct format: a number followed by it's unit of measurement (mm/cm/m), for example: 4.5m")


def parse_distance(distance: str) -> float:
    if distance.endswith("mm"):
        return float(distance[0:(len(distance) - 2)])

    if distance.endswith("cm"):
        return float(distance[0:(len(distance) - 2)]) * 10

    return float(distance[0:(len(distance) - 1)]) * 1000


if __name__ == "__main__":
    main()
