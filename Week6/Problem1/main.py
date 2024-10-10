# Implement a program that determines and displays the number of unique characters in a string entered by the user.
# For example, Hello, World! has 10 unique characters while zzz has only 1 unique character.
#
# Criteria:
# Use only dictionaries to solve this problem (create a function: unique_chars_dict).
# Use only sets to solve this problem (create a function: unique_chars_set).
# Make sure to implement both functions!
# Input example:
# Hello, World!
#
# Output example:
# Unique characters: 10

# Useless but ok.
def unique_chars_dict(sentence) -> int:
    return len({char: 0 for char in sentence})


def unique_chars_set(sentence) -> int:
    return len({char for char in sentence})


def main():
    sentence = input("Sentence: ")

    amount_of_unique_chars = unique_chars_set(sentence)

    print(f"Unique characters: {amount_of_unique_chars}")


if __name__ == "__main__":
    main()
