# Create an application that manages contacts in an addressbook.
#
# Menu structure:
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
# Criteria:
# Add a contact with first name and last name (only alphabet), multiple (unique) e-mails (containing at least one '@'), multiple (unique) phone numbers (only digits).
# Also, an ID should be generated which should be 1 higher than the highest current ID.
# Remove a contact by ID.
# List all contacts sorted by first_name in descending order.
# Merge duplicate contacts (when choosing [M] Merge contacts). Contacts with the exact same full name (first and last name combined) should be merged.
# The e-mails and phone numbers of the duplicate contacts should be added to the the first duplicate contact (contact with the highest ID).
# The other duplicate contcts should be deleted from the addressbook.
# Contacts are read from the provided JSON file and should be updated with new or removed contacts.
# Input example (add):
# A
# Firstname: John
# Lastname: Doe
# Emails: john@doe.com, john.doe@private.com
# Phonenumbers: 0612345678, 010-1234567
# Output example ([A] add):
# Contact added to addressbook
#
# Output example ([L] list contacts):
# ======================================
# Position:  1
# First name:  John
# Last name:  Doe
# Emails:  john@doe.com, john.doe@private.com
# Phone numbers:  0612345678, 010-1234567
# ======================================
# Position: 2
# First name: Peter
# Last name: Parker
# Emails: peter@parker.me
# Phone numbers: 0677345678
# ....

import json
import os
import re
import sys

'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''

DISPLAY_FORMAT = """======================================
Position: {}
First name: {}
Last name: {}
Emails: {}
Phone numbers: {}
"""


def display(addressbook: list):
    for entry in addressbook:
        emails = ", ".join(entry["emails"])
        phone_numbers = ", ".join(entry["phone_numbers"])

        print(DISPLAY_FORMAT.format(entry["id"], entry["first_name"], entry["last_name"], emails, phone_numbers))


def list_contacts(addressbook: list) -> list:
    sorted_addressbook = sorted(addressbook, key=lambda entry: entry["first_name"])

    display(sorted_addressbook)

    return sorted_addressbook


NAME_PATTERN = re.compile(r"([a-z]|[A-Z])+")
EMAILS_PATTERN = re.compile(r"(.+@.+|, )+")
PHONE_NUMBERS_PATTERN = re.compile(r"(\d+|, )+")


def add_contact(addressbook: list) -> list:
    first_name = request_input("Firstname: ", NAME_PATTERN)
    last_name = request_input("Lastname: ", NAME_PATTERN)
    emails = request_input("Emails: ", EMAILS_PATTERN)
    phone_numbers = request_input("Phonenumbers: ", PHONE_NUMBERS_PATTERN)

    new_entry = {
        "id": max((entry["id"] for entry in addressbook), default=0) + 1,
        "first_name": first_name,
        "last_name": last_name,
        "emails": emails.split(", "),
        "phone_numbers": phone_numbers.split(", ")
    }

    addressbook.append(new_entry)

    print("Contact added to addressbook")

    return addressbook


ID_PATTERN = re.compile(r"\d+")


def remove_contact(addressbook: list) -> list:
    entry_id = request_input("ID: ", ID_PATTERN)

    index = [entry["id"] for entry in addressbook].index(int(entry_id))

    del addressbook[index]

    return addressbook


def merge_contacts(addressbook: list) -> list:
    for key_a, entry_a in enumerate(addressbook):
        for key_b, entry_b in enumerate(addressbook[key_a + 1:]):
            same_first_names = entry_a["first_name"] == entry_b["first_name"]
            same_last_names = entry_a["last_name"] == entry_b["last_name"]

            if not same_first_names or not same_last_names:
                continue

            entry_a["emails"] += entry_b["emails"]
            entry_a["phone_numbers"] += entry_b["phone_numbers"]

            del addressbook[key_a + 1 + key_b]

    return addressbook


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def request_input(prompt: str, pattern: re.Pattern[str]):
    while True:
        unvalidated_input = input(prompt).strip()

        if pattern.fullmatch(unvalidated_input):
            return unvalidated_input

        print(f"Invalid entry, entry should match: {pattern.pattern}")


MENU_FORMAT = """[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program
"""


def main(json_file):
    addressbook = read_from_json(json_file)

    while True:
        addressbook, stop = loop(addressbook)

        if stop:
            write_to_json(json_file, addressbook)
            break


MENU_INPUT_PATTERN = re.compile("[larmqLARMQ]")


def loop(addressbook: list):
    print(MENU_FORMAT)

    action = request_input("Action: ", MENU_INPUT_PATTERN)

    match action.lower():
        case "l":
            addressbook = list_contacts(addressbook)
        case "a":
            addressbook = add_contact(addressbook)
        case "r":
            addressbook = remove_contact(addressbook)
        case "m":
            addressbook = merge_contacts(addressbook)
        case "q":
            return addressbook, True
        case _:
            print("Please enter one of the following actions: L/A/R/M/Q")

    return addressbook, False


if __name__ == "__main__":
    main('contacts.json')
