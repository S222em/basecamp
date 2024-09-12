# Implement a program that a user enters number of days as input, and the program prints number of hours, minutes and seconds separately as output.
#
# Input example:
# Days: 1
#
# Output example:
# Hours: 24, Minutes: 1440, Seconds: 86400

days = input("Days: ")

if not days.isdigit():
    print("Please enter a valid integer")
    exit()

days = int(days)

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
