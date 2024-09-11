# Implement a program that given a number of years as input prints the number of months and days as output.
#
# Criteria:
# keep the problem simple
# no leap year
# each year is 365 days and 12 months
# Expected Program Behaviour: After running the program, the program will wait for the user input. The user will enter the full string Years: 5.
# The program can provide a proper message to guide the user about the correct input format.
# The program must slice the input and extract the number to process and produce the result.

# Input example:
# Years: 5

# Output example:
# Months: 60, Days: 1825

import re

print("Please enter below in the following format: 'Years: x' ")
user_input = input()

if not re.search("Years: \d+", user_input):
    print("Please enter in the following format: 'Years: x' ")
    exit(0)

years = int(user_input.split()[1])

months = years * 12
days = years * 365

print(f"Months: {months}, Days: {days}")
