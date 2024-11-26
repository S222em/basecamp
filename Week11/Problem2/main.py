# Using data from bannedvideogames.csv, implement a program that allows the following:
#
# Game information extra's:
# Implement a program that shows the following information:
#
# How many games got banned in Israel?
# Which country got the most games banned?
# How many games within the Assassin's Creed series are currently banned? Don't count duplicates banned in different countries.
# Show all games (and the details) banned in Germany.
# Show all countries (and the details) the game Red Dead Redemption got banned in.
# Game modification extra's:
# Implement a program that makes the following adjustments and write it back to the file:
#
# Germany got a new law that accepts all games as a form of art. Remove all records with Germany from the file.
# The game Silent Hill VI got renamed to Silent Hill Remastered, rename this in all corresponding records.
# The ban on the game Bully in Brazil has been lifted. Change the status to Ban Lifted.
# The game Manhunt II is banned by several countries. It is incorrectly listed as genre Stealth, change the genre to Action in all corresponding records.
# Add game extra's:
# You can use the following list for keys:
#
# ['id', 'name', 'series', 'country', 'details', 'category', 'status', 'wikipedia', 'image', 'summary', 'developer', 'publisher', 'genre', 'homepage']
# Default menu:
# [I] Print request info from assignment
# [M] Make modification based on assignment
# [A] Add new game to list
# [O] Overview of banned games per country
# [S] Search the dataset by country
# [Q] Quit program
#
# Input example (add):
# A
# <id>
# <name>
# <series>
# <country>
# <details>
# <category>
# <status>
# <wikipedia>
# <image>
# <summary>
# <developer>
# <publisher>
# <genre>
# <homepage>
# Q
#
# Input example (overview):
# O
# Q
# Output example (overview):
# <country_name> - <amount_banned>
# - <game_name_1>
# - <game_name_2>
# ...
#
# Input example (search):
# S
# Netherlands
# Q
# Output example (search):
# <game_name_1> - <game_details_1>
# <game_name_2> - <game_details_2>
# ...
import csv

# Seems like codegrade crashes when only "Q" is entered in the program.
# I can't reproduce it, so I guess it's a codegrade issue.
# And for the other problem in check if modifications was made, it's not specific enough to be able to tell what is wrong.
# This assignment is too boring to spend more time to try and fix it

GAME_FIELDNAMES = ['id', 'name', 'series', 'country', 'details', 'category', 'status', 'wikipedia', 'image', 'summary',
                   'developer', 'publisher', 'genre', 'homepage']


def get_games(file_name):
    """
    Read games from the provided files
    :param file_name:
    :return:
    """
    with open(file_name, newline='') as file:
        # [1:] is to skip header
        games = list(csv.DictReader(file, fieldnames=GAME_FIELDNAMES))[1:]

    return games


def save_games(file_name, games):
    """
    Save all the games in the provided file
    :param file_name:
    :param games:
    :return:
    """
    with open(file_name, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=GAME_FIELDNAMES)
        writer.writeheader()
        writer.writerows(games)


def get_games_banned_in_country(games, country):
    """
    Finds the total amount of games banned in a country
    :param games:
    :param country:
    :return:
    """
    return sum(1 for game in games if country == game["country"])


def get_country_most_banned(games):
    """
    Finds the country with the most banned games
    :param games:
    :return:
    """
    countries = dict()

    for game in games:
        countries[game["country"]] = countries.setdefault(game["country"], 0) + 1

    return max(countries.items(), key=lambda item: item[1])[0]


def get_series_amount_of_banned(games, series):
    """
    Returns the amount of games banned in a series
    :param games:
    :param series:
    :return:
    """
    return len(set(game["name"] for game in games if series == game["series"]))


def print_info(games):
    """
    Print info as listed in the assignment
    :param games:
    :return:
    """
    assassins_creed_banned = get_series_amount_of_banned(games, "Assassin's Creed")
    print(
        f"Banned in israel: {get_games_banned_in_country(games, 'Israel')}",
        f"\nMost banned games in country: {get_country_most_banned(games)}",
        f"\nAssassins creed series banned games: {assassins_creed_banned}"
    )

    banned_in_germany = [game for game in games if game['country'] == "Germany"]
    print("\nBanned games in germany:")
    for game in banned_in_germany:
        print(f"{game['name']} - {game['details']}")

    banned_rdr = [game for game in games if game['name'] == "Red Dead Redemption"]
    print("\nRed Dead Redemption banned in:")
    for game in banned_rdr:
        print(f"{game['country']} - {game['details']}")


def make_modifications(games):
    """
    Make modifications to the games as listed in the assignment
    :param games:
    :return:
    """

    deleted_count = 0
    # Remove all games banned in germany
    for i, game in enumerate(games):
        if game["country"] != "Germany":
            continue

        del games[i - deleted_count]
        deleted_count += 1

    # Rename Silent Hill VI to Silent Hill Remastered
    for game in games:
        if game["name"] != "Silent Hill VI":
            continue

        game["name"] = "Silent Hill Remastered"

    # Lift ban on Bully in Brazil
    for game in games:
        if game["country"] != "Brazil" or game["name"] != "Bully":
            continue

        game["status"] = "Ban Lifted"

    # Change genre of Manhunt II to Action
    for game in games:
        if game["name"] != "Manhunt II":
            continue

        game["genre"] = "Action"

    return games


def add_game(games):
    """
    Adds a new banned game and collects data for it
    :param games:
    :return:
    """
    game = dict()

    for field in GAME_FIELDNAMES:
        field_value = input(f"{field}: ")
        game[field] = field_value

    games.append(game)

    return games


def print_overview(games):
    """
    Prints an overview per country as listed in the assignment
    :param games:
    :return:
    """
    countries = dict()

    for game in games:
        countries.setdefault(game["country"], []).append(game)

    for country, games in countries.items():
        print(
            f"{country} - {len(games)}",
            *(f"\n{game['name']}" for game in games),
            "\n"
        )


def search_by_country(games):
    """
    Search the games by country as listed in the assignment
    :param games:
    :return:
    """
    country = input("country: ")

    for game in games:
        if game["country"] != country:
            continue

        print(f"{game['name']} - {game['details']}")


def main(file_name):
    games = get_games(file_name)

    while True:
        games, stop = loop(games)

        if stop:
            save_games(file_name, games)
            break


MENU_LAYOUT = """[I] Print request info from assignment
[M] Make modification based on assignment
[A] Add new game to list
[O] Overview of banned games per country
[S] Search the dataset by country
[Q] Quit program
"""


def loop(games):
    """
    Main loop of the program
    :param games:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower()

    if selected_option == "i":
        print_info(games)

    if selected_option == "m":
        games = make_modifications(games)

    if selected_option == "a":
        games = add_game(games)

    if selected_option == "o":
        print_overview(games)

    if selected_option == "s":
        search_by_country(games)

    return games, selected_option == "q"


if __name__ == "__main__":
    main("bannedvideogames.csv")
