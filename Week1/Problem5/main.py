# Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
#
# Input example:
# 3141
#
# Output example:
# 3+1+4+1=9

numbers_str = input()

if not numbers_str.isdigit():
    print("Please enter a valid integer")
    exit(0)

numbers = [int(number) for number in numbers_str]

total_sum = sum(numbers)

print(f"{'+'.join([str(number) for number in numbers])}={total_sum}")
