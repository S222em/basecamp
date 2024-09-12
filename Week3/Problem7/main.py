# Do some research regarding truth tables.
# Use iterative programming to solve this problem to print the truth tables for and and or.
# Implement a program that prints these two truth tables.
#
# Criteria:
# Use 4 states: True + True, True + False, False + True, False + False
# Input example:
# No input is given
#
# Output example:
# AND
# True + True = True
# ...
#
# OR
# ...

for operator in "AND", "OR":
    print(operator)
    for a in True, False:
        for b in True, False:
            print(f"{a}+{b}={a and b if operator == 'AND' else a or b}")
