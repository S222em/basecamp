from datetime import datetime


def print_people(people):
    for person in people:
        number_and_name = f"{person['number']:7s} {person['firstname']:11s} {person['surname']:16s}"
        date_of_birth = f"{person['day']:02d}-{person['month']:02d}-{person['year']:4d}"
        print(number_and_name, date_of_birth)
    print("-" * 47)


def my_filter(func, iterable) -> list:
    filtered = []

    for value in iterable:
        if func(iterable):
            filtered.append(value)

    return filtered


def main():
    students = [
        {"number": "1075356", "firstname": "Abdulhameed", "surname": "Ahmad", "day": 5, "month": 6, "year": 1996},
        {"number": "1112338", "firstname": "Budi", "surname": "Waskito", "day": 6, "month": 7, "year": 2005},
        {"number": "0949275", "firstname": "Kira", "surname": "Jesus Gomes, de", "day": 11, "month": 3, "year": 2000},
        {"number": "2401592", "firstname": "Semih", "surname": "Küçük", "day": 11, "month": 2, "year": 2005},
        {"number": "1100080", "firstname": "Sten", "surname": "Nierop", "day": 26, "month": 10, "year": 2004},
        {"number": "1111303", "firstname": "Jamil", "surname": "Ree, van de", "day": 29, "month": 8, "year": 2003},
        {"number": "1102004", "firstname": "Sem", "surname": "Roeten", "day": 15, "month": 7, "year": 2006},
        {"number": "1096116", "firstname": "Rover", "surname": "Rot", "day": 14, "month": 3, "year": 2005},
        {"number": "1095917", "firstname": "Youri", "surname": "Schmitz", "day": 17, "month": 9, "year": 2006},
        {"number": "1089791", "firstname": "Krista", "surname": "Tauriņa", "day": 13, "month": 12, "year": 2005},
        {"number": "1099108", "firstname": "Salih", "surname": "Tokur", "day": 9, "month": 10, "year": 2001},
        {"number": "1105408", "firstname": "Lean", "surname": "Vreeswijk, van", "day": 29, "month": 11, "year": 2006},
        {"number": "1111300", "firstname": "Sivan", "surname": "Zechiel", "day": 6, "month": 5, "year": 2006},
        {"number": "1102086", "firstname": "Andi", "surname": "Zeng", "day": 20, "month": 11, "year": 2007},
    ]

    print("Sorted by number")
    students.sort(key=lambda student: student["number"])
    print_people(students)

    print("Sorted by firstname")
    students.sort(key=lambda student: student["firstname"])
    print_people(students)

    print("Sorted by firstname from the second letter")
    students.sort(key=lambda student: student["firstname"][1:])
    print_people(students)

    print("Sorted by reversed first name")
    students.sort(key=lambda student: student["firstname"][::-1])
    print_people(students)

    print("Sorted by age")
    students.sort(
        key=lambda student: (student["year"], student["month"], student["day"]),
    )
    print_people(students)

    print("Sorted by birthday")
    students.sort(
        key=lambda student: (student["month"], student["day"]),
    )
    print_people(students)

    print("Birthday in summer")
    birthday_in_summer = list(filter(lambda student: student["month"] in [7, 8], students))
    birthday_in_summer.sort(key=lambda student: (student["month"], student["day"]))
    print_people(birthday_in_summer)

    def filter_by_birthday_passed(student):
        now = datetime.now()

        if now.month > student["month"]:
            return True
        if now.month == student["month"] and now.day > student["day"]:
            return True

        return False

    print("Already had their birthdays")
    birthday_already_passed = list(filter(filter_by_birthday_passed, students))
    birthday_already_passed.sort(key=lambda student: (student["month"], student["day"]))
    print_people(birthday_already_passed)

    print("List of firstnames")
    firstnames = list(map(lambda student: student["firstname"], students))
    print(firstnames)


# 14. Schrijf een functie `my_map(func, iterable)` die hetzelfde doet als de functie `map()`


# 15. (Bonus) Maak een lijst met alle volledige namen
#     Tip 1: gebruik de functie `map()` met een wat complexere functie
#     Tip 2: om de achternaam goed te krijgen, kun je die splitsen op een komma,
#            het tuple omdraaien en dat omgedraaide tuple weer `join()`en met een spatie

if __name__ == "__main__":
    main()
