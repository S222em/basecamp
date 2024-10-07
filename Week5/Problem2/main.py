# When you take a taxi to a certain place, you pay for the amount of distance you traveled along with a basefare.
# Write a program that interacts with the user and calculates the fare of a taxi drive for a specified distance.
#
# Criteria:
# Base fare is 4.00 EUR
# Fare per 140 meter traveled is 0.25 EUR
# Use a function called calculate_fare(distance)
# that takes the distance in kilometers and returns the total fare as result
# Input examples:
# Distance traveled: 2
# Distance traveled: 1.4
# Output examples:
# Total fare: 7.75 EUR
# Total fare: 6.50 EUR
BASE_FARE = 4.0
FARE_PER_140_METERS = 0.25


# Not allowed to use math.ceil so this sucks
# Using floats for currency sucks but tests fail otherwise
def calculate_fare(distance):
    meters = distance * 1000

    amount_of_fares, remainder = divmod(meters, 140)

    fare = amount_of_fares * FARE_PER_140_METERS

    if remainder > 0:
        fare += FARE_PER_140_METERS

    return BASE_FARE + fare


def get_distance():
    distance = input("Distance traveled: ")

    return float(distance)


def main():
    distance = get_distance()
    fare = calculate_fare(distance)

    print(f"Total fare: {fare:.2f} EUR")


if __name__ == "__main__":
    main()
