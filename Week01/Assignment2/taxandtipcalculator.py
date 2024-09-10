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
