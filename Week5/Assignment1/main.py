# A dataset is given with information of students: student number, first name, last name, date of birth, study program. You are asked to implement a program that given this dataset (as a csv file), the program processes the information. Sometimes data values are corrupted. The program must report corrupted values.
#
# Criteria:
# Any invalid or empty value is defined as corrupted.
# Student number has this format: 7 digits, starting with 0 and second digit (from left) can be either 9 or 8.
# Example: 0212345 is not valid
# First name and last names, contains only alphabet.
# Date of birth has this format: YYYY-MM-DD. Days between 1 and 31, months between 1 and 12 and Years between 1960 and 2004.
# Study program can have one of these values: INF, TINF, CMD, AI.
# Extra:
# A template Python file is provided with a function that loads the data set.
# The program should make two separate lists: list of rows with correct values and a list of rows with corrupted values.
# Within the template the headers that are required are already present.
#
# Input example:
# No input is given
#
# Output example:
# ### VALID LINES ###
# 0997435,Tybi,Beavan,1955-08-04,AI
# 0959294,Aidan,Rennox,1982-09-15,TINF
# ...
# ### CORRUPT LINES ###
# 0959490,Abbe,Trees,1986-11-29,DS => INVALID DATA: ['DS']
# ,Mignon,Miners,1983-10-14, => INVALID DATA: ['', '']
# ...

import os
import re
import sys

STUDENT_NUMBER_PATTERN = re.compile(r"(08|09)\d{5}")
NAME_PATTERN = re.compile(r"[a-zA-Z]+")
DATE_PATTERN = re.compile(r"(19[6-9][0-9]|200[0-4])-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])")
STUDY_PROGRAM_PATTERN = re.compile(r"INF|TINF|CMD|AI")

valid_lines = []
corrupt_lines = []


def validate_data(line: str):
    corrupt_values = []

    [student_number, first_name, last_name, date_of_birth, study_program] = line.split(",")

    def validate_value(value, pattern):
        if not pattern.fullmatch(value):
            corrupt_values.append(value)

    validate_value(student_number, STUDENT_NUMBER_PATTERN)
    validate_value(first_name, NAME_PATTERN)
    validate_value(last_name, NAME_PATTERN)
    validate_value(date_of_birth, DATE_PATTERN)
    validate_value(study_program, STUDY_PROGRAM_PATTERN)

    if corrupt_values:
        corrupt_lines.append(f"{line} => INVALID DATA: {corrupt_values}")
    else:
        valid_lines.append(line)


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
