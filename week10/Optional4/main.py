# (Optional problem)
#
# Sensitive information is often removed, or redacted,
# from documents before they are released to the public.
# When the documents are released it is common for the redacted text to be replaced with black bars.
# In this exercise you will write a program that redacts all occurrences
# of sensitive words in a text file by replacing them with asterisks.
# Your program should redact sensitive words wherever they occur,
# even if they occur in the middle of another word.
# The list of sensitive words will be provided in a separate text file.
# Save the redacted version of the original text in a new file.
# The names of the original text file, sensitive words file, and redacted file will all be provided by the user.

def redact(text, sensitive_words):
    """
    Replaces all the words in the sensitive words list with *
    :param text:
    :param sensitive_words:
    :return:
    """
    for word in sensitive_words:
        text = text.replace(word, "*" * len(word))

    return text


def main(text_file_name, sensitive_file_name, redacted_file_name):
    try:
        with open(text_file_name) as text_file:
            text = text_file.read()

        with open(sensitive_file_name) as sensitive_file:
            sensitive_words = sensitive_file.readlines()

        redacted = redact(text, sensitive_words)

        with open(redacted_file_name, "w") as redacted_file:
            redacted_file.write(redacted)

    except IOError:
        print("Something went wrong while opening one of the files")


if __name__ == "__main__":
    main(input("Text: "), input("Sensitive words: "), input("Redacted: "))
