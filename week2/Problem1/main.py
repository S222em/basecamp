# Write a program that reads an integer from the user.
# Then your program should display a message indicating whether the integer is even or odd.
#
# Input examples:
# Number: 1
# Number: 4
# Output examples:
# Odd
# Even

number = input("Number: ")

if not number.isdigit():
    print("Please enter a valid integer")
    exit()

number = int(number)

print("Even" if number % 2 == 0 else "Odd")
