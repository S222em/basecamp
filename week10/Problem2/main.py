# In addition to head (A3W10P1), Unix-based operating systems also typically include a tool named tail.
# It displays the last 10 lines of a file whose name is provided as a command line parameter.
# Write a Python program that provides the same behavior.
#
# Note:
# There are several different approaches to solving this problem. Implement the three options and experiment with files with large content. Analyse the performance of each option (measure execution time of each solution).
#
# Options:
# is to load the entire contents of the file into a list and then display the last 10 elements.
# is to read the contents of the file twice, once to count the lines, and a second time to display the last 10 lines.
# Options one and two are not desirable when working with large files. Another solution exists that only requires you to read the file once, and only requires you to store 10 lines from the file at one time.
# Criteria:
# Use sys.argv to get the file from running
# Input example (correct):
# python3 tail.py randomfile.txt
#
# Output example (correct):
# this is line #91
# this is line #92
# this is line #93
# this is line #94
# this is line #95
# this is line #96
# this is line #97
# this is line #98
# this is line #99
# this is line #100
# Input example (error):
# blanc
#
# Output example (error):
# Error reading file: "blanc"
import os
import sys

BLOCK_SIZE = 256


def tail(file_name):
    """
    Returns the last 10 lines of the specified file
    :param file_name:
    :return:
    """

    lines = []
    blocks = 1

    with open(file_name, "rb") as file:
        while len(lines) <= 10:
            # Move our position back by BLOCK_SIZE * amount of blocks
            # Then see if the blocks contain at least 10 lines
            # If they do simply decode and return the last 10 lines
            # If not try again, adding another block
            file.seek(-blocks * BLOCK_SIZE, os.SEEK_END)
            lines = file.readlines()
            blocks += 1

    return "".join([line.decode('utf-8') for line in lines[-10:]])


def main(file_name):
    try:
        file_tail = tail(file_name)
        print(file_tail)
    except IOError:
        print(f'Error reading file: "{file_name}"')


if __name__ == "__main__":
    main(sys.argv[1])
