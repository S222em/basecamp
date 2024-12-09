# In this problem you are going to create a application to borrow and return books from a store/library
#
# Info:
# An existing dataset in JSON will be provided.
# The status of the books are in the database but the list of the books will be provided by JSON file.
#
# Extra:
# Initially, the program will check the content of JSON and compare it with the related table in the database.
# Then, missing elements must be inserted, the JSON file always has the latest update.
# After synchronising the file with the database, the program will have an interactive communication with the user.
#
# Default menu:
# [B] Borrow book
# [R] Return book
# [S] Search book
# [Q] Quit program
#
# Borrow book:
# Input: id or isbn and duration in days Extra: Should check if book is not borrowed at the moment
#
# statuses can be: AVAILABLE or BORROWED
# Output: date until this book can be borrowed
#
# calculate return_date based on (current_date + duration in days to borrow)
# Return book:
# Input: id or isbn Output: fine to pay (only if book is returned later then return date)
#
# 0.50 EUR per day that book is returned later then return date
# example: you borrow a book @ 29-11-2022 for 14 days, return_date should be 13-12-2022
# if you return it later (say 14-12-2022 you should have to pay 1 day * 0.50 EUR)
# Search book:
# Input: searchterm Extra: should search in title, isbn or author Output: should return book information + status_information
#
# statusses can be: AVAILABLE or BORROWED
# example: {'id': 1, 'isbn': '1010101010', 'title': 'Some title', 'author': 'Some Author', 'pages': 111, 'year': '2022', 'status': 'AVAILABLE', 'return_date': None}
import json
import math
import sqlite3
from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"


def dict_factory(cursor, row):
    """
    Creates a dictionary of the row
    :param cursor:
    :param row:
    :return:
    """
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def connect():
    """
    Connects to the database
    :return:
    """
    connection = sqlite3.connect("bookstore.db")
    connection.row_factory = dict_factory

    connection.execute(
        """CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );"""
    )

    return connection


def sync_books(connection):
    """
    Syncs the json file and the database
    :param connection:
    :return:
    """
    with open("books.json") as file:
        expected_books = json.load(file)

    query = """SELECT id, isbn FROM books"""

    cursor = connection.execute(query)

    actual_books = cursor.fetchall()

    done = set()

    # Go through every entry in the database and see if the book still exists in the json file
    # if so simply update it, otherwise delete it
    for book in actual_books:
        books = [b for b in expected_books if book["isbn"] == b["isbn"]]
        if len(books) == 0:
            delete_book(book["id"], connection)
            continue

        update_book(book["id"], books[0], connection)
        done.add(book["isbn"])

    # See which books in the json file don't exist yet and create them
    for book in expected_books:
        if book["isbn"] in done:
            continue

        create_book(book, connection)


def create_book(book, connection):
    """
    Creates a new book
    :param book:
    :param connection:
    :return:
    """
    query = """INSERT INTO books (isbn, title, author, pages, year) VALUES (:isbn, :title, :author, :pages, :year);"""

    connection.execute(query, book)


def update_book(id, book, connection):
    """
    Updates an existing book
    :param id:
    :param book:
    :param connection:
    :return:
    """
    query = """UPDATE books SET title=:title, author=:author, pages=:pages, year=:year WHERE id=:id;"""
    parameters = book | {"id": id}

    connection.execute(query, parameters)


def delete_book(id, connection):
    """
    Deletes a book
    :param id:
    :param connection:
    :return:
    """
    query = """DELETE FROM books WHERE id=?;"""
    parameters = (id,)

    connection.execute(query, parameters)


def update_book_status(id_or_isbn, status, return_date, connection):
    """
    Update a books status (status and return_date)
    :param id_or_isbn:
    :param status:
    :param return_date:
    :param connection:
    :return:
    """
    query = """UPDATE books SET status=:status, return_date=:return_date WHERE id=:id_or_isbn OR isbn=:id_or_isbn;"""
    parameters = {"id_or_isbn": id_or_isbn, "status": status, "return_date": return_date}

    connection.execute(query, parameters)


def main():
    """
    Main loop
    :return:
    """
    connection = connect()

    sync_books(connection)

    while True:
        stop = loop(connection)

        if stop:
            break

    connection.commit()
    connection.close()


def borrow_book(connection):
    """
    Borrow a book
    :param connection:
    :return:
    """
    id_or_isbn = input("Id or isbn: ")

    if not is_book_available(id_or_isbn, connection):
        return print(f"Book {id_or_isbn} is not available")

    duration = int(input("Duration (in days): "))

    date = datetime.now() + timedelta(days=duration)
    date = date.strftime(DATE_FORMAT)

    update_book_status(id_or_isbn, "BORROWED", date, connection)

    print(date)


def is_book_available(id_or_isbn, connection):
    """
    Whether the given id or isbn is available
    :param id_or_isbn:
    :param connection:
    :return:
    """
    query = """SELECT * FROM books WHERE (id=:id_or_isbn OR isbn=:id_or_isbn) AND status='AVAILABLE'"""
    parameters = {"id_or_isbn": id_or_isbn}

    cursor = connection.execute(query, parameters)
    rows = cursor.fetchall()

    return len(rows) == 1


def return_book(connection):
    """
    Return a book
    :param connection:
    :return:
    """
    id_or_isbn = input("Id or isbn: ")

    query = """SELECT * FROM books WHERE (id=:id_or_isbn OR isbn=:id_or_isbn) AND status='BORROWED'"""
    parameters = {"id_or_isbn": id_or_isbn}

    cursor = connection.execute(query, parameters)
    book = cursor.fetchone()

    if not book:
        return print(f"Book {id_or_isbn} is not borrowed")

    update_book_status(id_or_isbn, "AVAILABLE", None, connection)

    overdue = datetime.now() - datetime.strptime(book["return_date"], DATE_FORMAT)

    days_overdue = math.ceil(overdue.total_seconds() / 60 / 60 / 24)

    if days_overdue > 0:
        return print(f"Overdue, fee to pay: {days_overdue * 0.5:02f}EUR")

    print("Returned book")


def search_book(connection):
    """
    Searches for a book in isbn, title or author
    :param connection:
    :return:
    """
    search_term = input("Search term: ")

    query = """SELECT * FROM books WHERE isbn LIKE :term OR title LIKE :term OR author LIKE :term"""
    parameters = {"term": search_term + "%"}

    cursor = connection.execute(query, parameters)
    row = cursor.fetchone()

    print(row)


MENU_LAYOUT = """[B] Borrow book
[R] Return book
[S] Search book
[Q] Quit program
"""


def loop(connection):
    """
    Main loop
    :param connection:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower().strip()

    if selected_option == "b":
        borrow_book(connection)

    if selected_option == "r":
        return_book(connection)

    if selected_option == "s":
        search_book(connection)

    return selected_option == "q"


if __name__ == "__main__":
    main()
