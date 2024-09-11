# Consider a valid license plate in The Netherlands (see valid patterns below).
# Write a program that begins by reading a string of characters from the user.
# Then your program should display a message indicating whether the characters are representing a valid license plate.
#
# Valid patterns:
# XX-99-99 d
# 99-99-XX d
# 99-XX-99 d
# XX-99-XX d
# XX-XX-99 d
# 99-XX-XX d
# 99-XXX-9 d
# 9-XXX-99 d
# XX-999-X d
# X-999-XX d
# XXX-99-X
# 9-XX-999
# Input examples:
# License: A-149-HH
# License: 149-A-HH
# Output examples:
# Valid
# Invalid
import re

license_plate = input("License: ")

regex = [
    "[A-Z]{2}-[1-9]{2}-[1-9]{2}",
    "[1-9]{2}-[1-9]{2}-[A-Z]{2}",
    "[1-9]{2}-[A-Z]{2}-[1-9]{2}",
    "[A-Z]{2}-[1-9]{2}-[A-Z]{2}",
    "[A-Z]{2}-[A-Z]{2}-[1-9]{2}",
    "[1-9]{2}-[A-Z]{2}-[A-Z]{2}",
    "[1-9]{2}-[A-Z]{3}-[1-9]{1}",
    "[1-9]{1}-[A-Z]{3}-[1-9]{2}",
    "[A-Z]{2}-[1-9]{3}-[A-Z]{1}",
    "[A-Z]{1}-[1-9]{3}-[A-Z]{2}",
    "[A-Z]{3}-[1-9]{2}-[A-Z]{1}",
    "[1-9]{1}-[A-Z]{2}-[1-9]{3}",
]

print("Valid" if any(re.fullmatch(r, license_plate) for r in regex) else "Invalid")
