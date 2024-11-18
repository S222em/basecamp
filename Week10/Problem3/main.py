# In this exercise you will create a Python program that identifies the longest word(s) in a file.
#
# Extra:
# Treat any group of non-white space characters as a word, even if it includes numbers or punctuation marks.
#
# Input example (correct):
# randomtext.txt
#
# Output example (correct):
# Length of longest word(s) is [11] chars
# These are all the words of that length:
# discovered., continuing., everything., interested., favourable., themselves., solicitude
# Input example (error):
# blanc
#
# Output example (error):
# Error reading file: "blanc"


def find_longest_words(file_name):
    """
    Finds all words in a file that are the longest
    :param file_name:
    :return:
    """
    with open(file_name) as file:
        text = file.read()
        words = text.replace("\n", " ").split(" ")
        max_len = max(len(word) for word in words)
        return [word for word in words if len(word) == max_len]


def main(file_name):
    try:
        longest_words = find_longest_words(file_name)
        print(
            f"Length of longest word(s) is [{len(longest_words[0])}] chars",
            "\nThese are all the words of that length:",
            f"\n{', '.join(longest_words)}"
        )
    except IOError:
        print(f'Error reading file: "{file_name}"')


if __name__ == "__main__":
    main(input("File: "))
