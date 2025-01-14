# We are currently in a migration fase of changing our gradingsystem. To keep track of the results of a course and the results of students, we want to create a small Python application that stores this data for us.
#
# Extra:
# Each class should belong to it's own file:
# Student > student.py
# Course > course.py
# Result > result.py
# ResultsManager > resultsmanager.py
#
# Database:
# To keep track of this information you are given a database structure with a 3 tables:
# students
#
# id INTEGER (AUTO-INCREMENT)
# first_name TEXT
# last_name TEXT
# date_of_birth DATE
# class_code TEXT
# courses
#
# id INTEGER (AUTO-INCREMENT)
# name TEXT
# points INTEGER
# results
#
# student_id INTEGER
# course_id INTEGER
# mark INTEGER
# achieved DATE
#
# Class Student:
# Create a class corresponding to the table of students, make sure the id has None as default value and is set as the last parameter within the __init__()
#
# Class Course:
# Create a class corresponding to the table of courses, make sure the id has None as default value and is set as the last parameter within the __init__()
#
# Class Result:
# Create a class corresponding to the table of results.
#
#
# Class ResultsManager:
# We already created a class ResultsManager with the methods needed to make everything complete. It's your task to finish the functionality of this class so we can use it.
#
# Methods:
# def get_course(self, course_id) -> Course:
# This method will get the course from the database based on the course_id provided. Will return a Course object if a result was found else it should return None.
# def add_course(self, course: Course) -> Course:
# This method will add a course to the database, it should return the Course object updated with the id it got from the database so we can use it without calling the database again.
# def get_student(self, student_id) -> Student:
# This method will get the student from the database based on the student_id provided. Will return a Student object if a result was found else it should return None.
# def add_student(self, student: Student) -> Student:
# This method will add a student to the database, it should return the Student object updated with the id it got from the database so we can use it without calling the database again.
# def add_result(self, result: Result) -> bool:
# This method will add a result to the database. Before inserting the new result, you should check if the new mark for this student and course is higher than any previous mark. If not return False if succeeded return True
# def get_results_by_student(self, student_id, only_last=True):
# This method should grab all results from the database belonging to the given student_id, if only_last is False it should return all results for that student, if only_last is True (default) it should only return the highest mark per course for that student. It should return a list of tuples.
# def get_results_by_course(self, course_id, only_last=True):
# This method should grab all results from the database belonging to the given course_id, if only_last is False it should return all results for that course, if only_last is True (default) it should only return the highest mark per student for that course. It should return a list of tuples.

from resultsmanager import ResultsManager
from week15.problem3.course import Course
from week15.problem3.result import Result
from week15.problem3.student import Student


def main():
    manager = ResultsManager()
    manager.create_tables()

    dev101 = manager.get_course(1)

    if not dev101:
        dev101 = manager.add_course(Course("Development 101", 4))

    john = manager.get_student(1)

    if not john:
        john = manager.add_student(Student("John", "Doe", "2003-08-12", "BC11A"))
        manager.add_result(Result(john.id, dev101.id, 50, "2023-03-18"))
        manager.add_result(Result(john.id, dev101.id, 40, "2023-05-05"))  # should not be added
        manager.add_result(Result(john.id, dev101.id, 70, "2023-06-22"))

    print(manager.get_results_by_student(john.id))

    print(manager.get_results_by_course(dev101.id, False))

    manager.close()


if __name__ == "__main__":
    main()
