# {Optional problem}
#
# Spelling mistakes are only one of many different kinds of errors that might appear in a written work.
# Another error that is common for some writers is a repeated word.
# For example, an author might inadvertently duplicate a word,
# as shown in the following sentence:
#
# At least one value must be entered entered in order to compute the average.
# Some word processors will detect this error and identify it when a spelling or grammar check is performed.
# In this exercise you will write a program that detects repeated words in a text file.
# When a repeated word is found your program should display a message that contains the line number and the repeated word.
#
# Example:
# Found duplicate word [something] on line: 10
# Then the program must ask the user if the repeated word has to be removed or if it should find and display the next instance of a duplicate word. The name of the examined file will be provided as the program’s only command line parameter. Display an appropriate error message if the user fails to provide a command line parameter, or if an error occurs while processing the file.

class RepeatedWordRemover:
    """
    Tool to find all repeated words in a file and remove them
    """

    def __init__(self, file_name):
        """
        Creates a new instance
        :param file_name: The file to find repeated words in
        """

        self.lines = []
        self.position = (0, 0)
        self.file_name = file_name

        self._read()

    def _read(self):
        """
        Read the contents of the file
        :return:
        """
        with open(self.file_name) as file:
            self.lines = file.readlines()

    def _write(self):
        """
        Write the altered lines to the file
        :return:
        """
        with open(self.file_name, "w") as file:
            file.write("".join(self.lines))

    def _get_words(self):
        """
        Returns a list of words in the current line
        :return:
        """
        return self.lines[self.position[0]].strip().split(" ")

    def _get_line_iterator(self):
        """
        Returns an iterator over the not processed lines
        :return:
        """
        return enumerate(self.lines[self.position[0]:])

    def _get_word_iterator(self, words):
        """
        Returns an iterator ovr the not processed words in the current line
        :param words:
        :return:
        """
        return enumerate(words[self.position[1] + 1:])

    def next(self):
        """
        Finds the next duplicate if any
        In case there are no more duplicates the altered lines are written to the file
        :return:
        """
        for i, line in self._get_line_iterator():
            words = self._get_words()
            for j, word in self._get_word_iterator(words):
                if word.lower() != words[self.position[1] + j].lower():
                    continue

                self.position = self.position[0] + i, self.position[1] + j + 1
                return word

        self._write()
        return None

    def remove(self):
        """
        Removes the current duplicate from the line
        :return:
        """
        words = self._get_words()
        del words[self.position[1]]
        self.position = self.position[0], self.position[1] - 1
        self.lines[self.position[0]] = " ".join(words) + "\n"


def main(file_name):
    if not file_name:
        return print("Missing file parameter")

    try:
        repeated_word_remover = RepeatedWordRemover(file_name)
        while True:
            stop = loop(repeated_word_remover)

            if stop:
                break

    except IOError:
        return print(f"Unable to read {file_name}")


OPTION_MENU = """[remove] Remove the duplicate
[continue/enter] Go to next duplicate
"""


def loop(repeated_word_remover):
    word = repeated_word_remover.next()

    if word is None:
        return True

    print(f"Found duplicate word [{word}] on line: {repeated_word_remover.position[0] + 1}")
    selected = input(OPTION_MENU).lower()

    if selected == "remove":
        repeated_word_remover.remove()


if __name__ == "__main__":
    main(input("File: "))
