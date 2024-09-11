# Write a program that reads a date from the user and computes its immediate successor.
#
# Criteria:
# The date will be entered in YYYY-MM-DD format.
# Assume there is no leap year so February always has 28 days.
# The program must employ a function is_input_valid(inp_date) that checks if the provided input satisfies the expected format. The function returns true if the input has correct format. In case of incorrect format, the function must return false.
# The program must print Input format ERROR. Correct Format: YYYY-MM-DD in case the user enters an incorrect input.
#
# Some examples of incorrect input: 2013/12/30, 2013_12_30, 0213/12/30, 30-12-2013.
#
# Input examples:
# Input Date: 2013-11-18
# Input Date: 2013-11-30
# Input Date: 2013-12-31
# Output examples:
# Next Date: 2013-11-19
# Next Date: 2013-12-01
# Next Date: 2014-01-01

MONTH_LENGTH = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
]

user_input = input("Input Date: ")


def is_input_valid(inp_date: str):
    numbers = inp_date.split("-")
    # If there are not exactly 3 elements in the list then the input is invalid
    if len(numbers) != 3: return False
    # If the list does not contain strings with only numbers in them the input is invalid
    if not all(number.isdigit() for number in numbers): return False

    [possible_year, possible_month, possible_day] = [int(number) for number in numbers]

    # Check if the provided date is in bounds
    if possible_year < 0 or possible_month < 0 or possible_month > 12 or possible_day < 0 or possible_day > \
            MONTH_LENGTH[possible_month - 1]: return False

    return True


if not is_input_valid(user_input):
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
    exit(0)

# Parse the input to integers
[year, month, day] = [int(number) for number in user_input.split("-")]

day += 1

if day > MONTH_LENGTH[month - 1]:
    day = 1
    month += 1

if month > 12:
    month = 1
    year += 1

print(f"Next Date: {year}-{month:02d}-{day:02d}")
