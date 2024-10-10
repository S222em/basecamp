# Implement a Python program that collects book information.
#
# Criteria:
# Entering new book: The program will ask to enter: book title, book author, publisher, publication date
# Input will be (comma seperated, single line). A book title can only be added to the list once (no duplication)
# Searching a book: The user enters a term and the program must search the term within titles, authors and publishers and report the existence of such a book with the requested term.
# Create a function called: search_book(books, term) which will return True or False on a match or not
# Use a list of dictionaries for datastorage with the following attribute fields: [title, author, publisher, pub_date]
# Default menu:
# [A] Add book
# [S] Search book
# [E] Exit (and print)
# Input example (entering new book):
# Book details: harry potter,rowling,bloomsbury,1997
#
# Output example (entering new book):
# Book has been added
#
# Input example (searching a book):
# Sarch term: rowling
#
# Output example (searching a book):
# Found a book for: rowling
#
# Output example (exiting):
# {'title': 'Clean Code', 'author': 'Martin Robert', 'publisher': 'Financial Times Prentice Hall', 'pub_date': '2008'}
# {'title': 'The Clean Coder', 'author': 'Martin Robert', 'publisher': 'Financial Times Prentice Hall', 'pub_date': '2011'}

DEFAULT_MENU = """[A] Add book
[S] Search book
[E] Exit (and print)"""


def get_action():
    print(DEFAULT_MENU)
    return input("Action: ")


def add_book(books: list[dict[str, str]], book_info: str) -> bool:
    book_info = book_info.split(",")

    if any(book["title"] == book_info[0] for book in books):
        return False

    books.append({
        "title": book_info[0],
        "author": book_info[1],
        "publisher": book_info[2],
        "pub_date": book_info[3]
    })

    return True


def search_book(books: list[dict[str, str]], term: str) -> bool:
    possible_match = next((book for book in books if any(term in value for value in book.values())), None)

    return possible_match is not None


def on_exit(books: list[dict]):
    for book in books:
        print(book)


def loop(books: list[dict[str, str]]):
    action = get_action()

    if action == "A":
        book_info = input("Book details (book title,book author,publisher,publication date): ").lower()
        print("Book has been added" if add_book(books, book_info) else "Book already exists")

    if action == "S":
        term = input("Search term: ").lower()
        if search_book(books, term):
            print(f"Found a book for: {term}")
        else:
            print(f"Could not find a book for: {term}")

    if action == "E":
        on_exit(books)
        return True


def main():
    books = list()

    while True:
        stop = loop(books)

        if stop:
            break


if __name__ == "__main__":
    main()
