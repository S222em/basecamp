# In this exercise, you will create a program that removes all of the comments from a Python source file.
#
# Extra:
# Python uses the # character to mark the beginning of a comment.
# The comment ends at the end of the line containing the # character.
# Check each line in the file to determine if a # character is present. If it is then your program should remove all of the characters from the # character to the end of the line (we’ll ignore the situation where the comment character occurs inside of a string).
# The user will also enter the name of the input file.
# Save the modified file using a new name that will be entered by the user.
# Input example (correct):
# File to read: functiontest.txt
# File to save: cleaned-functiontest.txt
#
# Output example (correct):
# No output should be given
#
# Input example (error):
# blanc
#
# Output example (error):
# Error reading file: "blanc"

def remove_comments(lines):
    """
    Removes all lines that are comments
    :param lines:
    :return:
    """
    i = 0
    while i != len(lines):
        line = lines[i]
        if not line.startswith("#"):
            i += 1

        del lines[i]

    return lines


def main(read_file_name, save_file_name):
    try:
        with open(read_file_name) as read_file:
            comments_removed = remove_comments(read_file.readlines())

            with open(save_file_name, "wt") as save_file:
                save_file.write("\n".join(comments_removed))

    except IOError:
        print(f'Error reading file: "{read_file_name}"')


if __name__ == "__main__":
    main(input("File to read: "), input("File to save: "))
