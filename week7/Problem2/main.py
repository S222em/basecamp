# A data file containing Netflix title is provided.
#
# Menu structure:
# [1] Print the amount of TV Shows
# [2] Print the amount of Movies
# [3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.
#     (for example, search the name David Ayer. He is the director of three movies and one tv show)
#     Treat multitple directors (seperated by comma) as 1 single director!
# [4] Print the name of each director in alphabetical order,
#     the number of movies and the number of tv shows (s)he was the director of.
#     Use a tuple with format: (director name, number of movies, number of tv shows) to print.
# Criteria:
# The program gets the file name as a program argument.
# Use the function load_csv_file to load the content of the file in a list.
# The first line of the file specifies the name of each column.
# For example, the first column is show_id, the second is the type of the show, etc...
# Create a function called get_headers(file_content) that returns a list of all the columns from the first row (explore the kind of information you can extract)
# Make a function search_by_type(file_content, show_type) that returns a list of all TV Shows or Movies based on the requested type
# Make use of lambda for the solution
# Make a function search_by_director(file_content, director) that returns a list of all TV Shows and Movies that have that director
# Make use of lambda for the solution
# Make a function get_directors(file_content) that returns a set of directors in the list (use set for single directors only)
# Treat multitple directors (seperated by comma) as 1 single director!
# Input example:
# 4
#
# Output example:
# [('A. L. Vijay', 2, 0), ('A. Raajdheep', 1, 0), ...

import csv
import os
import sys


def get_headers(netflix_titles) -> list:
    """
    Returns the headers of the csv file
    """
    return netflix_titles[0]


def search_by_type(netflix_titles, show_type) -> list:
    """
    Find all occurrences of the specified show type in the cvs file
    """
    return list(filter(
        lambda title: show_type in title[1],
        netflix_titles,
    ))


def search_by_director(netflix_titles, director) -> list:
    """
    Finds all the titles a director has directed
    """
    return list(filter(
        lambda title: director == title[3],
        netflix_titles,
    ))


def get_directors(netflix_titles) -> set:
    """
    Returns a set of all directors
    """
    return set(map(
        lambda title: title[3],
        netflix_titles[1::]
    ))


def load_csv_file(file_name: str) -> list:
    """
    Loads and parses the csv file into lists
    """
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


def director_movie_and_tv_shows(director, netflix_titles) -> (int, int):
    """
    Counts the amount of movies and tv_shows a director has directed
    (movies, tv_shows)
    """
    directed = search_by_director(netflix_titles, director)

    movies = search_by_type(directed, "Movie")
    tv_shows = search_by_type(directed, "TV Show")

    return len(movies), len(tv_shows)


def directs_movie_and_tv_show(director, netflix_titles):
    """
    Whether a director directs both a movie and a tv_show
    """
    (movies, tv_shows) = director_movie_and_tv_shows(director, netflix_titles)

    return movies > 0 and tv_shows > 0


MENU_LAYOUT = """
[1] Print the amount of TV Shows
[2] Print the amount of Movies
[3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.
   (for example, search the name David Ayer. He is the director of three movies and one tv show)
    Treat multitple directors (seperated by comma) as 1 single director!
[4] Print the name of each director in alphabetical order,
    the number of movies and the number of tv shows (s)he was the director of.
    Use a tuple with format: (director name, number of movies, number of tv shows) to print.
"""


def main(file_name: str):
    netflix_titles = load_csv_file(file_name)

    selected_menu_option = input(MENU_LAYOUT)

    if selected_menu_option == "1":
        print(len(search_by_type(netflix_titles, "TV Show")))

    if selected_menu_option == "2":
        print(len(search_by_type(netflix_titles, "Movie")))

    if selected_menu_option == "3":
        directors = get_directors(netflix_titles)

        filtered_directors = list(filter(
            lambda director: director and directs_movie_and_tv_show(director, netflix_titles),
            directors
        ))

        filtered_directors.sort()

        print(filtered_directors)

    if selected_menu_option == "4":
        directors = list(get_directors(netflix_titles))

        directors.sort()

        directors_movies_and_tv_shows = list()

        for director in directors:
            (movies, tv_shows) = director_movie_and_tv_shows(director, netflix_titles)
            directors_movies_and_tv_shows.append((director, movies, tv_shows))

        print(directors_movies_and_tv_shows)


if __name__ == "__main__":
    main("netflix_titles.csv")
