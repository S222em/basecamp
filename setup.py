#!/usr/bin/env python3

import os


def create_directory_with_file(directory: str):
    if os.path.isdir(directory): return

    os.makedirs(directory)
    file = os.path.join(directory, "main.py")
    open(file, "x")


def main():
    week = int(input("Week: "))
    problems = int(input("Amount of problems: "))
    optional = int(input("Amount of optional problems: "))
    assignments = int(input("Amount of assignments: "))

    basecamp_directory = os.path.dirname(os.path.abspath(__file__))
    week_directory = os.path.join(basecamp_directory, f"week{week}")

    os.makedirs(week_directory, exist_ok=True)

    for i in range(problems):
        problem_directory = os.path.join(week_directory, f"problem{i + 1}")
        create_directory_with_file(problem_directory)

    for i in range(optional):
        optional_directory = os.path.join(week_directory, f"optional{i + 1}")
        create_directory_with_file(optional_directory)

    for i in range(assignments):
        assignment_directory = os.path.join(week_directory, f"assignment{i + 1}")
        create_directory_with_file(assignment_directory)


if __name__ == "__main__":
    main()
