import json
import os
import sqlite3
import sys
from sqlite3 import Cursor

from transaction import Transaction


class FinanceApp:
    def __init__(self, db_name='finance.db'):
        self.connection = sqlite3.connect(os.path.join(sys.path[0], db_name))
        self.cursor = self.connection.cursor()

    def build_database(self):
        """
        Builds the database
        :return:
        """
        self.cursor.execute("DROP TABLE IF EXISTS transactions")
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT ,
                            date TEXT,
                            description TEXT,
                            category TEXT,
                            amount REAL);''')
        self.connection.commit()

    def load_transactions_from_json(self, json_file):
        """
        Loads all the transactions from the given json file
        :param json_file:
        :return:
        """
        with open(os.path.join(sys.path[0], json_file), 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        for transaction in json_data:
            date = transaction["date"]
            description = transaction["description"]
            category = transaction["category"]
            amount = transaction["amount"]
            self.add_transaction(date, description, category, amount, commit=False)

        self.connection.commit()

    def execute(self, query, parameters, commit=True) -> Cursor:
        """
        Executes a query and commits if needed
        Returns the cursor
        :param query:
        :param parameters:
        :param commit:
        :return:
        """
        self.cursor.execute(query, parameters if parameters else ())
        if commit:
            self.connection.commit()

        return self.cursor

    def add_transaction(self, date, description, category, amount, commit=True) -> Transaction:
        """
        Adds a transaction
        :param date:
        :param description:
        :param category:
        :param amount:
        :param commit:
        :return:
        """
        query = """INSERT INTO transactions
                    (date, description, category, amount)
                    VALUES (?, ?, ?, ?);"""
        parameters = (date, description, category, amount)

        transaction_id = self.execute(query, parameters, commit).lastrowid

        return Transaction(transaction_id, date, description, category, amount)

    def update_transaction(self, transaction_id, date, description, category, amount, commit=True) -> bool:
        """
        Updates a transaction
        Empty values are ignored
        :param transaction_id:
        :param date:
        :param description:
        :param category:
        :param amount:
        :param commit:
        :return:
        """
        query = """UPDATE transactions SET
                    date=ifnull(?, date),
                    description=ifnull(?, description),
                    category=ifnull(?, category),
                    amount=ifnull(?, amount)
                    WHERE id=?;"""

        parameters = (
            date if date else None,
            description if description else None,
            category if category else None,
            amount if amount else None,
            transaction_id
        )

        return self.execute(query, parameters, commit).rowcount == 1

    def delete_transaction(self, transaction_id, commit=True) -> bool:
        """
        Deletes a transaction
        :param transaction_id:
        :param commit:
        :return:
        """
        query = """DELETE FROM transactions WHERE id=?"""
        parameters = (transaction_id,)

        return self.execute(query, parameters, commit).rowcount == 1

    def search_transactions(self, term: str) -> list[Transaction]:
        """
        Searches for given term in category and description
        :param term:
        :return:
        """
        query = """SELECT * FROM transactions WHERE category LIKE :term OR description LIKE :term;"""
        parameters = {"term": term}

        rows = self.execute(query, parameters, commit=False).fetchall()

        return [Transaction(*row) for row in rows]

    def get_transactions(self, year: str | None = None) -> list[Transaction]:
        """
        Returns all transactions in a specific year, or all transactions if no year is given
        :param year:
        :return:
        """
        query = """SELECT * FROM transactions WHERE :year IS NULL OR date LIKE :year;"""
        parameters = {"year": f"%{year}%" if year else None}

        rows = self.execute(query, parameters, commit=False).fetchall()

        return [Transaction(*row) for row in rows]

    def get_total_income(self, year: str | None = None):
        """
        Returns the total income in a year, or over all years if no year is given
        :param year:
        :return:
        """
        query = """SELECT SUM(amount) FROM transactions WHERE (:year IS NULL OR date LIKE :year) AND category='Work';"""
        parameters = {"year": f"%{year}%" if year else None}

        row = self.execute(query, parameters, commit=False).fetchone()

        return round(row[0], 2)

    def get_total_expenses(self, year: str | None = None):
        """
        Returns the total expenses in a year, or over all years if no year is given
        :param year:
        :return:
        """
        query = """SELECT SUM(amount) FROM transactions WHERE
                    (:year IS NULL OR date LIKE :year)
                    AND amount < 0
                    AND category != 'Work'
                    AND category != 'Savings';"""
        parameters = {"year": f"%{year}%" if year else None}

        row = self.execute(query, parameters, commit=False).fetchone()

        return round(row[0], 2)

    def get_total_savings(self, year: str | None = None):
        """
        Returns the total savings made in a year, or in all years if no year is given
        :param year:
        :return:
        """
        query = """SELECT SUM(amount) FROM transactions WHERE (:year IS NULL OR date LIKE :year)
                    AND category = 'Savings';"""
        parameters = {"year": f"%{year}%" if year else None}

        row = self.execute(query, parameters, commit=False).fetchone()

        return -round(row[0], 2)

    def get_expenses(self) -> list[tuple[str, float]]:
        """
        Returns the expenses per category
        :return:
        """
        query = """SELECT category, amount FROM transactions WHERE amount <= 0;"""

        rows = self.execute(query, None, commit=False).fetchall()

        categories = dict()

        for category, amount in rows:
            categories[category] = categories.setdefault(category, 0) + amount

        return list((category, round(amount, 2)) for category, amount in categories.items())

    def get_savings(self) -> list[tuple[str, float]]:
        """
        Returns the savings made per year
        :return:
        """
        query = """SELECT date, amount FROM transactions WHERE category='Savings';"""

        rows = self.execute(query, None, commit=False).fetchall()

        years = dict()

        for date, amount in rows:
            # If only I could have used defaultdict ):
            years[date[-4:]] = years.setdefault(date[-4:], 0) - amount

        return list((year, round(amount, 2)) for year, amount in years.items())

    def count_transactions(self, year: str | None = None) -> int:
        """
        Counts transactions made in a year, or all years if no year is given
        :param year:
        :return:
        """
        query = """SELECT COUNT(*) FROM transactions WHERE :year IS NULL OR date LIKE :year;"""
        parameters = {"year": f"%{year}" if year else None}

        rows = self.execute(query, parameters, commit=False).fetchall()

        return rows[0][0]

    def get_report(self, year: str | None = None) -> dict[str, float]:
        """
        Creates a report of income, expenses, savings and the total between them
        :param year:
        :return:
        """
        income = self.get_total_income(year)
        expenses = self.get_total_expenses(year)
        savings = self.get_total_savings(year)
        total = round(income + expenses + savings, 2)

        return {
            "transactions": self.count_transactions(year),
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "total": total
        }
