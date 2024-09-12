# Positions on a chess board are identified by a letter and a number.
# Usually, the letter identifies the column, while the number identifies the row.
# Write a program that reads a position from the user.
# The program should determine if the column begins with a black square or a white square.
# Then use modular arithmetic (check if you know this concept) to report the color of the square in that row.
#
# Criteria:
# Your program may assume that a valid position will always be entered
# Input examples:
# Position: D5
# Position: A1
# Output examples:
# White
# Black
import re

position = input("Position (example: A2): ").lower()

if not re.fullmatch("[a-z]\d", position):
    print("Please enter a valid chessboard position (A2)")
    exit()

[letter, number] = position

# Replaces character a-z to 1-26
letter = ord(letter) - 96
number = int(number)

# True = White, False = Black
start_color = letter % 2 == 0

# If the number is even it's the opposite of the row start color
# If the number is uneven it's equal to the row start color
color = not start_color if number % 2 == 0 else start_color

print("White" if color else "Black")
