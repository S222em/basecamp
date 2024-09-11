# Write a program that draws “modular rectangles” like the ones below.
# The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom, but are all done mod 10.
#
# Input example:
# Width: 5
# Height: 3
#
# Output example:
# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4
import textwrap

# Tests fail if a prompt is present
width = int(input())
height = int(input())

characters = [str(i % 10) for i in range(width * height)]

lines = textwrap.wrap(" ".join(characters), width=width * 2)

print(" \n".join(lines))
