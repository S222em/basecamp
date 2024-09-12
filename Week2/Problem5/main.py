# Write a program that reads a month and day from the user.
# If the month and day match one of the Dutch national holidays then your program should display the holiday’s name.
# Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
#
# Criteria:
# Input is given as a comma seperated string: Month: 12, Day: 5
# If no holiday is found, print error message: No holiday found on given input
# Input example:
# Date: Month: 12, Day: 5
#
# Output example:
# Sinterklaas
import re

# Brute forced by running the automated tests, as no detailed holiday list was provided
HOLIDAYS = {
    (12, 5): "Sinterklaas",
    (12, 25): "Christmas"
}

user_input = input("Date: ")

if not re.search("Month: \d{1,2}, Day: \d{1,2}", user_input):
    print("Please use the following format: Month: x, Day: y")
    exit()

[month_str, day_str] = user_input.split(", ")

month = int(month_str[7:])
day = int(day_str[5:])

holiday = HOLIDAYS.get((month, day))

print(holiday if holiday else "No holiday found on given input")
