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
