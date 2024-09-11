#!/usr/bin/env python3

import os


def validate_and_parse(string: str):
    if string.isdigit(): return int(string)

    print("Please enter a valid integer")
    exit(0)


week = validate_and_parse(input("Week: "))
problems = validate_and_parse(input("Amount of problems: "))
assignments = validate_and_parse(input("Amount of assignments: "))

basecamp_directory = os.path.dirname(os.path.abspath(__file__))
week_directory = os.path.join(basecamp_directory, f"Week{week}")

os.makedirs(week_directory, exist_ok=True)

def create_directory_with_file(directory: str):
    if os.path.isdir(directory): return

    os.makedirs(directory)
    file = os.path.join(directory, "main.py")
    open(file, "x")

for i in range(problems):
    problem_directory = os.path.join(week_directory, f"Problem{i + 1}")
    create_directory_with_file(problem_directory)

for i in range(assignments):
    assignment_directory = os.path.join(week_directory, f"Assignment{i + 1}")
    create_directory_with_file(assignment_directory)

