contacts = []


def add_contact(name, phone_number, email):
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(contact)


def search_by_name(name):
    return list(filter(lambda c: name.lower() in c['name'].lower(), contacts))


def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)


def test():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    assert len(contacts) == 1
    assert contacts[0]['name'] == "John Doe"

    search_results = search_by_name("John")
    assert search_results[0]['name'] == "John Doe"

    delete_contact("John Doe")
    assert len(contacts) == 0

    print("All tests are executed.")


if __name__ == "__main__":
    test()
