# In a program a function is implemented to traverse the folders and files.
# It returns the result as a list. A list indicates a folder and a string item is a file.
#
# For example: ['file_1',[]] is a folder that contains a file and an empty subfolder; ['file_1','file_2',['file_1']] is a folder containing two files and a subfolder with a file.
# Your task is to implement a Python function that:
#
# Given such a list as the root folder prints the contents. Indentation of the folder will be > and for a file it will be -.
# Given such a list as the root folder prints the number of files.
#
# Below you will see the result of the execution for the first two cases:
#
# Folder_0
#  file_1
# >Folder_1
# Number of files in case:  ['file_1', []]  is  1
# Folder_0
#  file_1
#  file_2
# >Folder_1
# - file_1
# Number of files in case:  ['file_1', 'file_2', ['file_1']]  is  3

def rec_print_folders(n: int, pref: str, root: list) -> None:
    """
    This function prints the contents of a given root folder with indentations.
    """
    print(f"{'>' * n}Folder_{n}")

    for item in root:
        if isinstance(item, str):
            print(f"{'-' * n} {item}")
            continue

        rec_print_folders(n + 1, pref, item)


def rec_count_files(root: list) -> int:
    """
    The functions counts number of files in a given folder (and all its sub-folders).
    :param root: A nested list: an element either is a file (name) or a list as a sub-folder.
    :return:
    """
    total = 0

    for item in root:
        # The item is a file, increment the counter
        if isinstance(item, str):
            total += 1
            continue

        # The item is a folder, recursively count the amount of files in the folder
        total += rec_count_files(item)

    return total


def main():
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'],
         ['file_6', ['file_7', 'file_8'], ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]
    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))


if __name__ == "__main__":
    main()
