# The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user.
# Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing.
# The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip.
#
# Criteria:
# Tip is 15 percent of meal amount (without the tax)
# Assume a local tax rate of 21 percent
# Round all numbers to 3 decimals in the output
# Expected Behaviour: After running your code, it should print the following to the standard output and wait for the user input: Please enter the cost (format 'Cost of the meal: xy.wz'):
#
# Input example:
# Cost of the meal: 23.60
#
# Output example:
# Tax: 4.956 , Tip: 3.540 , Total: 32.096

import re

user_input = input("Please enter the cost (format 'Cost of the meal: xy.wz'): ")

if not re.search("Cost of the meal: \d+.\d+", user_input):
    print("Please use the format: 'Cost of the meal: xy.wz'")
    exit(0)

cost = float(user_input.replace("Cost of the meal: ", ""))
tax = cost * 0.21
tip = cost * 0.15
total = cost + tax + tip

print(f"Tax: {tax:.3f} , Tip: {tip:.3f} , Total: {total:.3f}")
