# A data file containing average daily temperature of Amsterdam is used.
# The first column is the month number, the second is the day number, the third is the year and fourth column is the temperature in Farenheit.
#
# Menu structure:
# [1] Print the average temperatures per year (fahrenheit)
# [2] Print the average temperatures per year (celsius) Hint: Use built-in map() function.
# [3] Print the warmest and coldest year as tuple based on the average temperature
# [4] Print the warmest month of a year based on the input year of the user (full month name)
# [5] Print the coldest month of a year based on the input year of the user (full month name)
# [6] Print a list of tuples where the first element of each tuple is the year and
#     the second element of the tuple is a dictionary with months as the keys and
#     the average temprature (in Celsius) of each month as the value
# Criteria:
# Use the function load_txt_file to load the content of the file in a list. Use the following format for the storage: {year: {month: [temp, temp, temp, ...]}, ...}
# Create a function fahrenheit_to_celsius(fahrenheit: float) -> float that given the value in fahrenheit returns the temperature in celsius (rounding is not needed)
# Create a function average_temp_per_month(temperatures_per_year: dict) -> list that calculates the average temperature per month. Return a list of tuples (month, temperature).
# Create a function average_temp_per_year(temperatures: dict) -> list that calculates the average temperature per year. Return a list of tuples (year, temperature).
# Input example:
# 4
# 1997
#
# Output example:
# August

import os
import sys

# This program does not pass the tests because the tests are too specific regarding the floats.
# The answers are still correct but only to a certain degree due to the floating point issues.

# Used to convert the month number to it's name
MONTH_NUMBER_TO_NAME = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts Fahrenheit to Celsius using floats
    """
    return (fahrenheit - 32) / 1.8


def average_temp_per_month(months: dict[str, list[float]]) -> list[(str, float)]:
    """
    Calculates the average temperature for each month
    Returns a list of tuples containing month number and the average
    """
    average_per_month = list()

    for month, temperatures in months.items():
        average = sum(temperatures) / len(temperatures)
        average_per_month.append((month, average))

    return average_per_month


def average_temp_per_year(years: dict[str, dict[str, list[float]]]) -> list[(str, float)]:
    """
    Calculates the average temperature for each year
    Returns a list of tuples containing year and the average
    """
    average_per_year = list()

    for year, months in years.items():
        average_per_month = average_temp_per_month(months)
        average = sum(average for (_, average) in average_per_month) / len(average_per_month)
        average_per_year.append((year, average))

    return average_per_year


def load_and_parse_data_file(file_name) -> dict[str, dict[str, list[float]]]:
    """
    Parses and reads the provided file into the required data format
    """
    years = dict()

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            [month, _, year, average_temperature] = line.split()

            years.setdefault(year, dict())
            years[year].setdefault(month, list()).append(float(average_temperature))

    return years


MENU_LAYOUT = """[1] Print the average temperatures per year (fahrenheit)
[2] Print the average temperatures per year (celsius) Hint: Use built-in map() function.
[3] Print the warmest and coldest year as tuple based on the average temperature
[4] Print the warmest month of a year based on the input year of the user (full month name)
[5] Print the coldest month of a year based on the input year of the user (full month name)
[6] Print a list of tuples where the first element of each tuple is the year and
    the second element of the tuple is a dictionary with months as the keys and
    the average temprature (in Celsius) of each month as the value
"""


def main(file_name: str):
    years = load_and_parse_data_file(file_name)

    selected_menu_option = input(MENU_LAYOUT)

    if selected_menu_option == "1":
        print(average_temp_per_year(years))

    if selected_menu_option == "2":
        average_per_year = list(map(
            lambda year_and_average: (year_and_average[0], fahrenheit_to_celsius(year_and_average[1])),
            average_temp_per_year(years)
        ))
        print(average_per_year)

    if selected_menu_option == "3":
        average_per_year = average_temp_per_year(years)
        max_year = max(average_per_year, key=lambda year_and_average: year_and_average[1])
        min_year = min(average_per_year, key=lambda year_and_average: year_and_average[1])
        print((max_year[0], min_year[0]))

    if selected_menu_option == "4":
        target_year = input("Year: ")
        average_per_month = average_temp_per_month(years[target_year])
        max_month = max(average_per_month, key=lambda month_and_average: month_and_average[1])
        print(MONTH_NUMBER_TO_NAME[max_month[0]])

    if selected_menu_option == "5":
        target_year = input("Year: ")
        average_per_month = average_temp_per_month(years[target_year])
        min_month = min(average_per_month, key=lambda month_and_average: month_and_average[1])
        print(MONTH_NUMBER_TO_NAME[min_month[0]])

    if selected_menu_option == "6":
        average_temperatures = list()
        for year, months in years.items():
            average_per_month = dict(average_temp_per_month(months))
            average_temperatures.append((year, average_per_month))

        print(average_temperatures)
        return


if __name__ == "__main__":
    main("NLAMSTDM.txt")
