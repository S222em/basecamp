# (Optional problem)
#
# A password that contains random characters is a relatively secure password, but it is also difficult to memorize.
# As an alternative, some systems construct a password by taking two English words and concatenating them.
# While this password isn’t as secure, it is much easier to memorize.
# Write a program that reads a file (from input) containing a list of words, randomly selects two of them, and concatenates them to produce a new password.
# When producing the password ensure that it has a minimum of 8 and a maximum of 10 characters, and that each word used is at least three letters long.
# Capitalize each word in the password so that the user can easily see where one word ends and the next one begins.
# Print the password for the user.
import random


def make_password(file_name):
    """
    Creates a new password consisting of two words in the provided file
    :param file_name:
    :return:
    """
    try:
        with open(file_name) as file:
            lines = file.readlines()
            left_filtered_lines = [line for line in lines if len(line.strip()) >= 3]
            left = random.choice(left_filtered_lines).strip()

            right_filtered_lines = [line for line in lines if 10 - len(left) >= len(line.strip()) >= 8 - len(left)]
            right = random.choice(right_filtered_lines).strip()
            return left.lower() + right.upper()
    except IOError:
        return f"Unable to open {file_name}"


if __name__ == "__main__":
    print(make_password(input("File: ")))
