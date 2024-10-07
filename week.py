#!/usr/bin/env python3

import os

def main():
    week = int(input("Week: "))
    problems = int(input("Amount of problems: "))
    assignments = int(input("Amount of assignments: "))

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

if __name__ == "__main__":
    main()