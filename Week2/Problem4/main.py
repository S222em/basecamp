# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.
#
# Criteria:
# Input is given as a comma separated string: a=5, b=6, c=5
# All 3 sides of an equilateral triangle have the same length.
# An isosceles triangle has two sides that are the same length, and a third side that is a different length.
# If all the sides have different lengths then the triangle is scalene.
# Input example:
# Sides: a=5, b=6, c=5
#
# Output example:
# Isosceles triangle

from collections import Counter

NAMES = ["Scalene triangle", "Isosceles triangle", "Equilateral triangle"]

sides = input("Sides: ")

try:
    sides = [int(side[2::]) for side in sides.split(", ")]

    counts = Counter(sides)

    max_count = max(counts.values())

    print(NAMES[max_count - 1])

except ValueError:
    print("Please enter valid integers (format: a=x, b=y)")
