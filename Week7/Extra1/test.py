from main import search_by_name, delete_contact, add_contact, contacts


def test_add_contact():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    assert len(contacts) == 1
    assert contacts[0]['name'] == "John Doe"
    contacts.clear()


def test_search_by_name():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    search_results = search_by_name("John")
    assert search_results[0]['name'] == "John Doe"
    contacts.clear()


def test_delete_contact():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    delete_contact("John Doe")
    assert len(contacts) == 0
