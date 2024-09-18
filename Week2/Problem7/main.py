import re


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
def main():
    position = input("Position (example: A2): ").lower()

    if not re.fullmatch("[a-h][1-8]", position):
        return print("Please enter a valid chessboard position (A2)")

    [letter, number] = position

    # Replaces character a-z to 1-26 (https://en.wikipedia.org/wiki/List_of_Unicode_characters)
    letter_as_number = ord(letter) - 96
    number = int(number)

    # The colour of a given square can be found by using the evenness of the column and row number.
    # If the column number is even, the square at a given column at row 1 will be white, otherwise black.
    # If the row number is even, it's colour will be the opposite as the column number evenness.
    is_column_even = letter_as_number % 2 == 0
    is_row_even = number % 2 == 0

    # If the result is True, the color is white, otherwise black.
    color_as_bool = not is_column_even if is_row_even else is_column_even

    print("White" if color_as_bool else "Black")


if __name__ == "__main__":
    main()
