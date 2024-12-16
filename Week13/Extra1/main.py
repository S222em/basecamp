# Osiris V1
# =========
# Hack this program and set your score for BaseCamp to "Passed"!
# Rules:
# 1. Understand this program and the database
# 2. Only run this program as often as you want and try different inputs
# 3. Do not change this program
# 4. Do not update the database yourself
# 5. Pretend you only know your own password (your student number)
# 6. You win when your score for course BaseCamp is "Passed"
# Happy hacking!

import sqlite3


def dict_factory(cursor, row):
    names = [column[0] for column in cursor.description]
    return dict(zip(names, row))


class OsirisV1:
    def __init__(self):
        self.database = sqlite3.connect("osiris.db")
        self.database.row_factory = dict_factory

    def __del__(self):
        self.database.close()

    def login(self) -> dict:
        while True:
            print("Log in")
            name = input("Name: ")
            password = input("Password: ")
            query = f"""
                SELECT *
                FROM users
                WHERE name='{name}' AND password='{password}'
            """
            print(query)
            try:
                user = self.database.execute(query).fetchone()
            except sqlite3.OperationalError as ex:
                print(f"ERROR: Invalid name / password ({ex})")
                user = None
            if user:
                break
            print("The combination name / password is not found")
        return user

    def update_grade(self) -> None:
        print("Update grade")
        name = input("Name: ")
        course = input("Course: ")
        score = input("Score: ")
        update_statement = """
            UPDATE grades
            SET score=?
            WHERE name=? AND course=?
        """
        self.database.execute(update_statement, [score, name, course])
        self.database.commit()
        print()

    def show_grades(self, user: dict) -> None:
        print("Show grades")
        select_grades = """
            SELECT *
            FROM grades
            WHERE name=?
        """
        grades = self.database.execute(select_grades, [user["name"]]).fetchall()
        for grade in grades:
            print(f"-> {grade['name']} scored {grade['score']} for {grade['course']}")
        print()


if __name__ == "__main__":
    osiris = OsirisV1()
    while True:
        user = osiris.login()
        print(f"You are logged in as {user['role']} {user['name']} and {user['status']}")
        print()
        if user['role'] == 'teacher':
            osiris.update_grade()
        elif user['role'] == 'student':
            osiris.show_grades(user)
        print("Logged out")
        print()
