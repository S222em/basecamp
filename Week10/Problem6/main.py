# When you write a function, it is a good idea to include a comment that outlines the function’s purpose, its parameters and its return value. However, sometimes comments are forgotten, or left out by well-intentioned programmers that plan to write them later but then never get around to it.
#
#
# Create a python program that reads one or more Python source files and identifies functions that are not immediately preceded by a comment.
#
# Extra:
# For the purposes of this exercise, assume that any line that begins with def, followed by a space, is the beginning of a function definition.
# Assume that the comment character, #, will be the first character on the previous line when the function has a comment.
# Display the names of all of the functions that do not have a comment, along with the file name and line number where the function definition is located.
# The user will provide the names of one or more Python files as command line parameters (comma separated).
# Input example (correct):
# functiontest.txt
#
# Output example (correct):
# File: functiontest.txt contains a function [function_name_here()] on line [1] without a preceding comment.
# File: functiontest.txt contains a function [another_function_name_here()] on line [15] without a preceding comment.
# Input example (error):
# functiontest.txt, blanc
#
# Output example (error):
# File: functiontest.txt contains a function [function_name_here()] on line [1] without a preceding comment.
# File: functiontest.txt contains a function [another_function_name_here()] on line [15] without a preceding comment.
# Error reading file: "blanc"

def find_functions_without_comment(lines: list[str]):
    """
    Finds all functions without a preceding comment
    :param lines:
    :return:
    """
    functions_without_comment = []

    for i in range(len(lines)):
        if not lines[i].startswith("def "):
            continue

        if i == 0 or not lines[i - 1].startswith("#"):
            function_name = lines[i][4:].split('(', 1)[0]
            functions_without_comment.append((function_name, i + 1))

    return functions_without_comment


def find_functions_without_comment_for_file(file_name):
    """
    Finds all the functions in the given file that do not have a preceding comment
    :param file_name:
    :return:
    """
    try:
        with open(file_name) as file:
            functions_without_comment = find_functions_without_comment(file.readlines())
            for function_name, line_number in functions_without_comment:
                print(
                    f'File: {file_name} contains a function [{function_name}()]',
                    f' on line [{line_number}] without a preceding comment.'
                )
    except IOError:
        print(f'Error reading file: "{file_name}"')


def main(file_names: str):
    for file_name in file_names.split(","):
        find_functions_without_comment_for_file(file_name.strip())


if __name__ == "__main__":
    main(input("Files (, separated): "))
