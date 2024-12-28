# Create a program that sorts a list of strings.
# Depending on the purpose of the sorting, the criteria of sorting can be different: alphabetically based on the first letter, length of the string, etc.
# Use the code template below and implement sorting based on the number of vowels (descending) within a string.
# For example, fall will occur before free.

# As just "VOWELS" is not clear enough apparently
VOWELS_AS_IN_VOWELS = ["a", "e", "i", "o", "u"]


def get_num_of_vowels(inp: str) -> int:
    """
    Returns the number of vowels in the input
    :param inp:
    :return:
    """
    return sum(char in VOWELS_AS_IN_VOWELS for char in inp)


def sort_basedon_vowels():
    words = ['code', 'programming', 'description', 'fly', 'free']
    print(sorted(words, key=get_num_of_vowels))


if __name__ == "__main__":
    sort_basedon_vowels()
