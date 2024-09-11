# Write a program that determines the name of a shape from its number of sides.
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message.
#
# Criteria:
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside of this range is entered then your program should display the error message: Amount of sides is out of range.
# Input examples:
# Sides: 3
# Sides: 4
# Output examples:
# Triangle
# Square

NAMES = [
    "Triangle",
    "Square",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon"
]

sides = input("Sides: ")

if not sides.isdigit():
    print("Please enter a valid integer")
    exit(0)

sides = int(sides)

if sides < 3 or sides > 10:
    print("Amount of sides is out of range")
    exit(0)

name = NAMES[sides - 3]

print(name)
