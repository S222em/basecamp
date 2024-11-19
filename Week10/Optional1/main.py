# (Optional problem)
#
# Create a program that adds line numbers to a file.
# The name of the input file will be read from the user,
# as will the name of the new file that your program will create.
# Each line in the output file should begin with the line number,
# followed by a colon and a space, followed by the line from the input file.

def add_line_numbers(file_name, save_name):
    """
    Adds line numbers to the given file and saves it
    :param file_name: The file to add line numbers to
    :param save_name: The new file to save in
    :return:
    """
    lines = []
    with open(file_name) as file:
        for i, line in enumerate(file.readlines()):
            lines.append(f"{i + 1}: {line}")

    with open(save_name, "w") as file:
        file.write("".join(lines))


if __name__ == "__main__":
    add_line_numbers(input("File: "), input("Save file: "))
