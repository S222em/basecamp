import os
import sqlite3
import sys

from course import Course
from result import Result
from student import Student


class ResultsManager:
    """
    Used to manage results
    """

    def __init__(self):
        self.connection = sqlite3.connect(
            os.path.join(sys.path[0], 'studentresults.db')
        )
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        Creates tables in the database if they don't yet exist
        :return:
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          points INTEGER NOT NULL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          first_name TEXT NOT NULL,
                          last_name TEXT NOT NULL,
                          date_of_birth DATE NOT NULL,
                          class_code TEXT NULL);''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS results
                         (student_id INTEGER NOT NULL,
                          course_id INTEGER NOT NULL,
                          mark INTEGER NOT NULL,
                          achieved DATE NOT NULL,
                          PRIMARY KEY(student_id, course_id, mark));''')

        self.connection.commit()

    def get_course(self, course_id) -> Course:
        """
        Retrieves a course from the database
        :param course_id:
        :return:
        """
        query = "SELECT name, points, id FROM courses WHERE id=?;"
        parameters = (course_id,)

        row = self.cursor.execute(query, parameters).fetchone()

        return Course(*row) if row else None

    def add_course(self, course: Course) -> Course:
        """
        Adds a course to the database
        :param course:
        :return:
        """
        query = "INSERT INTO courses (name, points) VALUES (?, ?);"
        parameters = (course.name, course.points)

        self.cursor.execute(query, parameters)
        self.connection.commit()

        course.id = self.cursor.lastrowid

        return course

    def get_student(self, student_id) -> Student:
        """
        Retrieves a student from the database
        :param student_id:
        :return:
        """
        query = "SELECT first_name, last_name, date_of_birth, class_code, id FROM students WHERE id=?;"
        parameters = (student_id,)

        row = self.cursor.execute(query, parameters).fetchone()

        return Student(*row) if row else None

    def add_student(self, student: Student) -> Student:
        """
        Adds a student to the database
        :param student:
        :return:
        """
        query = "INSERT INTO students (first_name, last_name, date_of_birth, class_code) VALUES (?, ?, ?, ?);"
        parameters = (student.first_name, student.last_name, student.date_of_birth, student.class_code)

        self.cursor.execute(query, parameters)
        self.connection.commit()

        student.id = self.cursor.lastrowid

        return student

    def get_highest_mark_for(self, student_id, course_id):
        query = "SELECT MAX(mark) FROM results WHERE student_id=? AND course_id=?;"
        parameters = (student_id, course_id)

        row = self.cursor.execute(query, parameters).fetchone()

        return row[0] if row and row[0] else 0

    def add_result(self, result: Result) -> bool:
        """
        Adds a result to the database
        :param result:
        :return:
        """
        if result.mark < self.get_highest_mark_for(result.student_id, result.course_id):
            return False

        query = "INSERT INTO results (student_id, course_id, mark, achieved) VALUES (?, ?, ?, ?)"
        parameters = (result.student_id, result.course_id, result.mark, result.achieved)

        self.cursor.execute(query, parameters)
        self.connection.commit()

        return True

    def get_results_by_student(self, student_id, only_last=True):
        """
        Returns all results of a student as a list of tuples.
        God knows why it has to be a list of tuples and not Result?
        :param student_id:
        :param only_last:
        :return:
        """
        if not only_last:
            query = "SELECT * FROM results WHERE student_id=?;"
            parameters = (student_id,)

            return self.cursor.execute(query, parameters).fetchall()

        query = """SELECT * FROM results WHERE student_id=:id AND mark = (
                        SELECT MAX(mark) FROM results WHERE student_id=:id GROUP BY course_id
                    );"""

        parameters = {"id": student_id}

        return self.cursor.execute(query, parameters).fetchall()

    def get_results_by_course(self, course_id, only_last=True):
        """
        Returns all results of a course as a list of tuples.
        God knows why it has to be a list of tuples and not Result?
        :param course_id:
        :param only_last:
        :return:
        """
        if not only_last:
            query = "SELECT * FROM results WHERE course_id=?;"
            parameters = (course_id,)

            return self.cursor.execute(query, parameters).fetchall()

        query = """SELECT * FROM results WHERE course_id=:id AND mark = (
                        SELECT MAX(mark) FROM results WHERE course_id=:id GROUP BY student_id
                    );"""

        parameters = {"id": course_id}

        return self.cursor.execute(query, parameters).fetchall()

    def close(self):
        self.connection.close()
