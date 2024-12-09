# In this problem you are going to create an application to organise students and their info by class
#
# Extra:
# You can use the the provided code (see template) to connect with the database and create it if it does not exist.
#
# Default menu:
# [A] Add new student
# [C] Assign student to class
# [D] List all students
# [L] List all students in class
# [S] Search student
# [Q] Quit program
#
# Add new student:
# Input: first_name, last_name, city, date_of_birth (DD-MM-YYYY), class (optional)
# Output: return the assigned studentnumber (auto-created)
#
# Assign student to class:
# Input: studentnumber (primary_key), class
# Error (if student was not found): Could not find student with number: {studentnumber}
#
# List all students:
# Input: None
# Output: should be sorted based on class in descending order
#
# List all students in class:
# Input: class to search students in
# Output: should be sorted based on studentnumber in ascending order
#
# Search student:
# Input: searchterm and search in first_name, last_name or city
# Output: limit result to 1

import sqlite3


def connect():
    """
    Connects to the database
    :return:
    """
    # autocommit was added in 3.12 and codegrade uses 3.11 ):
    connection = sqlite3.connect("studentdatabase.db")

    connection.execute(
        """CREATE TABLE IF NOT EXISTS students (
            studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city TEXT NOT NULL,
            date_of_birth DATE NOT NULL,
            class TEXT DEFAULT NULL
        );"""
    )

    return connection


def main():
    """
    The main program
    :return:
    """
    connection = connect()

    while True:
        stop = loop(connection)

        if stop:
            break

    connection.commit()
    connection.close()


def add_student(connection):
    """
    Adds a new student to the database
    :param connection:
    :return:
    """
    first_name = input("First name: ")
    last_name = input("Last name: ")
    city = input("City: ")
    date_of_birth = input("Date of birth (DD-MM-YYYY): ")
    student_class = input("Class (optional): ")

    query = """INSERT INTO students (first_name, last_name, city, date_of_birth, class) VALUES (?, ?, ?, ?, ?);"""
    parameters = (first_name, last_name, city, date_of_birth, student_class if student_class else "NULL")

    cursor = connection.execute(query, parameters)

    print(f"Created student {cursor.lastrowid}")


def assign_class(connection):
    """
    Assigns a class to a student
    :param connection:
    :return:
    """
    student_number = input("Student number: ")
    student_class = input("Class: ")

    query = """UPDATE students SET class=? WHERE studentnumber=?"""
    parameters = (student_class, student_number)

    cursor = connection.execute(query, parameters)

    if cursor.rowcount <= 0:
        return print(f"Could not find student with number: {student_number}")

    print(f"Added student {student_number} to class {student_class}")


def list_students(connection):
    """
    Lists all students sorted by class
    :param connection:
    :return:
    """
    query = """SELECT * FROM students ORDER BY class DESC;"""

    cursor = connection.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def list_students_in_class(connection):
    """
    Lists all students in a class sorted by student number
    :param connection:
    :return:
    """
    student_class = input("Class: ")

    query = """SELECT * FROM students WHERE class=? ORDER BY studentnumber ASC;"""
    parameters = (student_class,)

    cursor = connection.execute(query, parameters)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def search_student(connection):
    """
    Searches for a student with given term, searches in first_name, last_name and city
    :param connection:
    :return:
    """
    search_term = input("Search term: ")

    query = """SELECT * FROM students WHERE first_name LIKE :term OR last_name LIKE :term OR city LIKE :term;"""
    parameters = {"term": search_term + '%'}

    cursor = connection.execute(query, parameters)
    row = cursor.fetchone()

    print(row)


MENU_LAYOUT = """[A] Add new student
[C] Assign student to class
[D] List all students
[L] List all students in class
[S] Search student
[Q] Quit program
"""


def loop(connection):
    """
    Main loop
    :param connection:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower().strip()

    if selected_option == "a":
        add_student(connection)

    if selected_option == "c":
        assign_class(connection)

    if selected_option == "d":
        list_students(connection)

    if selected_option == "l":
        list_students_in_class(connection)

    if selected_option == "s":
        search_student(connection)

    return selected_option == "q"


if __name__ == "__main__":
    main()
