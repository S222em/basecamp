# It is commonly said that one human year is equivalent to 7 dog years.
# However, this simple conversion fails to recognize that dogs reach adulthood in approximately two years.
# As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.
# Write a program that implements the conversion from human years to dog years described in the previous paragraph.
#
# Criteria:
# First 2 human years are 10.5 dog years per human year
# Each extra human year is 4 dog years per human year
# Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years
# Your program should display an error message Only positive numbers are allowed if the user enters a negative number
# Input examples:
# Human years: 1
# Human years: 4
# Human years: -1
# Output examples:
# Dog years: 10.5
# Dog years: 29
# Only positive numbers are allowed

human_years = input("Human years: ")

if not human_years.isdigit() and not human_years.startswith("-"):
    print("Please enter a valid integer")
    exit()

human_years = int(human_years)

if human_years < 0:
    print("Only positive numbers are allowed")
    exit()

dog_years = sum([4.0 if i > 1 else 10.5 for i in range(human_years)])

print(f"{dog_years:.1f}")
