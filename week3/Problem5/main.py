# In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10.
#
# Criteria:
# Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10.
# It should also include labels down the left side consisting of the numbers 1 through 10.
# Input:
# No input is given
#
# Output example:
#    1  2  3  4  5  6  7  8  9 10
# 1  1  2  3  4  5  6  7  8  9 10
# 2  2  4  6  8 10 12 14 16 18 20
# ...

LABELS = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
ITEM_LENGTH = 3

rows = [LABELS]

for i in range(1, 11):
    row = [str(i)]

    for j in range(1, 11):
        row.append(str(i * j))

    rows.append(row)

print("\n".join("".join(item.ljust(ITEM_LENGTH) for item in row) for row in rows))
