# Write a program that displays the word (or words) that occur most and least frequently in a file.
#
# Extra:
# Your program should begin by reading the name of the file from the user.
# Then it should find the word(s) by splitting each line in the file at each space.
# Finally, any leading or trailing punctuation marks should be removed from each word.
# In addition, your program should ignore capitalization.
# As a result, apple, apple!, Apple and ApPlE should all be treated as the same word.
# Input example (correct):
# randomtext.txt
#
# Output example (correct):
# Most: ['so']
# Least: ['understood', 'remarkably', 'solicitude', 'mean', 'them', ...]
# Input example (error):
# blanc
#
# Output example (error):
# Error reading file: "blanc"


def get_word_occurrences(file_name):
    """
    Counts the occurrences of all words in given file
    :param file_name:
    :return:
    """
    with open(file_name) as file:
        text = file.read().lower()
        words = text.replace("\n", " ").split(" ")
        # It's stupid I am not allowed to use string.punctuation as now I have to copy-paste it from
        # the python docs for no reason
        stripped = [word.strip(r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~") for word in words]
        occurrences = dict()

        for word in stripped:
            if len(word) == 0:
                continue

            occurrences[word] = occurrences.setdefault(word, 0) + 1

        return occurrences


def main(file_name):
    try:
        word_occurrences = get_word_occurrences(file_name)
        min_count = min(word_occurrences.values())
        max_count = max(word_occurrences.values())
        least = [word for word, count in word_occurrences.items() if count == min_count]
        most = [word for word, count in word_occurrences.items() if count == max_count]

        print(
            f"Most: {most}",
            f"\nLeast: {least}"
        )

    except IOError:
        print(f'Error reading file: "{file_name}"')


if __name__ == "__main__":
    main(input("File: "))
