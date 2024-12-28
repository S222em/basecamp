# Create a program that can handle movie information from the movies.json file
#
# Movie information extra's:
# Implement a program that uses the data from movies.json, and shows the following information:
#
# The number of movies released in 2004.
# The number of movies in which the genre is Science Fiction.
# All movies with actor Keanu Reeves.
# All movies with actor Sylvester Stallone released between 1995 and 2005.
# Movie modification extra's:
# Using data from movies.json, make the following adjustments and write it back to the file:
#
# Change the release year of the movie Gladiator from 2000 to 2001.
# Set the release year of the oldest movie to one year earlier.
# Actor Natalie Portman changed her name to Nat Portman. Adjust this for all movies she is in.
# Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.
# Default menu:
# [I] Movie information overview
# [M] Make modification based on assignment
# [S] Search a movie title
# [C] Change title and/or release year by search on title
# [Q] Quit program
#
# Input example (search):
# S
# Bambi
# Q
# Output example (search):
# {'title': 'Bambi', 'year': 1942, 'cast': ['Bambi'], 'genres': ['Children','Action']}
#
#
# Input example (modify):
# C
# Bambi
# Bambi Remastered
# 2023
# Q
# Output example (modify):
# {'title': 'Bambi Remastered', 'year': 2023, 'cast': ['Bambi'], 'genres': ['Children','Action']}
import json


class Searcher:
    """
    Utility to search a list of movies
    """

    def __init__(self, movies):
        """
        Instantiate a new searcher
        :param movies:
        """
        self._movies = iter(movies)

    def filter(self, func):
        """
        Filter the movies by provided func
        :param func:
        :return:
        """
        self._movies = filter(func, self._movies)
        return self

    def title(self, title):
        """
        Filter by the given title
        :param title:
        :return:
        """
        return self.filter(lambda movie: title == movie["title"])

    def year(self, year_or_range):
        """
        Filter by the given year or by the given year range
        :param year_or_range:
        :return:
        """
        years = year_or_range if isinstance(year_or_range, range) else range(year_or_range, year_or_range + 1)
        return self.filter(lambda movie: movie["year"] in years)

    def actor(self, actor):
        """
        Filter by the given actor
        :param actor:
        :return:
        """
        return self.filter(lambda movie: actor in movie["cast"])

    def genre(self, genre):
        """
        Filter by the given genre
        :param genre:
        :return:
        """
        return self.filter(lambda movie: genre in movie["genres"])

    def oldest(self):
        """
        Find the oldest movie in this searcher
        :return:
        """
        return min(self._movies, key=lambda movie: movie["year"])

    def count(self):
        """
        Count all movies still present in this searcher
        :return:
        """
        return sum(1 for _ in self._movies)

    def next(self):
        """
        Return the next movie in this searcher
        Returns None if the iterator is empty
        :return:
        """
        return next(self._movies, None)

    def collect(self):
        """
        Collects all iterators into a list and returns it
        :return:
        """
        return list(self._movies)


def information_overview(movies):
    """
    The information overview of the menu
    :param movies:
    :return:
    """
    movies_released_2004 = Searcher(movies).year(2004).count()
    movies_genre_science_fiction = Searcher(movies).genre("Science Fiction").count()
    movies_actor_keanu_reeves = Searcher(movies).actor("Keanu Reeves").collect()
    movies_actor_sylvester_stallone = Searcher(movies) \
        .year(range(1995, 2006)) \
        .actor("Sylvester Stallone") \
        .collect()

    print(
        f"Number of movies released in 2004: {movies_released_2004}",
        f"\nNumber of movies with genre Science Fiction: {movies_genre_science_fiction}",
        f"\nNumber of movies with actor Keanu Reeves: {movies_actor_keanu_reeves}"
        f"\nNumber of movies with Sylvester Stallone between 1995 and 2005: {movies_actor_sylvester_stallone}"
    )


def make_modifications(movies):
    """
    Makes modification to the movies as listed in the assignment
    :param movies:
    :return:
    """
    Searcher(movies).title("Gladiator").next().update({"year": 2001})

    oldest = Searcher(movies).oldest()
    oldest.update({"year": oldest["year"] - 1})

    movies_with_natalie = Searcher(movies).actor("Natalie Portman")
    while movie := movies_with_natalie.next():
        index = movie["cast"].index("Natalie Portman")
        movie["cast"][index] = "Nat Portman"

    movies_with_kevin = Searcher(movies).actor("Kevin Spacey")
    while movie := movies_with_kevin.next():
        movie["cast"].remove("Kevin Spacey")


def search(movies):
    """
    Searches for a movie by title
    :param movies:
    :return:
    """
    title = input("Title: ")
    movie = Searcher(movies).title(title).next()
    print(movie)


def change(movies):
    """
    Changes the title and/or year of a given title
    :param movies:
    :return:
    """
    title = input("Title: ")
    movie = Searcher(movies).title(title).next()

    new_title = input("New title (leave empty to skip): ")
    if new_title:
        movie["title"] = new_title

    new_year = input("New year released (leave empty to skip): ")
    if new_year:
        movie["year"] = int(new_year)


def main():
    with open("movies.json") as file:
        movies = json.load(file)

    while True:
        stop = loop(movies)

        if stop:
            with open("movies.json", "w") as file:
                file.write(json.dumps(movies))

            break


MENU_LAYOUT = """[I] Movie information overview
[M] Make modification based on assignment
[S] Search a movie title
[C] Change title and/or release year by search on title
[Q] Quit program
"""


def loop(movies):
    """
    Main loop of the program
    :param movies:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower()

    if selected_option == "i":
        information_overview(movies)
        return

    if selected_option == "m":
        make_modifications(movies)
        return

    if selected_option == "s":
        search(movies)
        return

    if selected_option == "c":
        change(movies)
        return

    if selected_option == "q":
        return True

    print("Please select a valid option.")


if __name__ == "__main__":
    main()
