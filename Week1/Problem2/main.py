# Implement a program that given number of years as input prints the number of months and days as output.
#
# Criteria:
# keep the problem simple
# no leap year
# each year is 365 days and 12 months
# Input example:
# Years: 5
#
# Output example:
# Months: 60, Days: 1825

years = input("Years: ")

if not years.isdigit():
    print("Please enter a valid integer number")
    exit(0)

years = int(years)

months = years * 12
days = years * 365

print(f"Months: {months}, Days: {days}")
