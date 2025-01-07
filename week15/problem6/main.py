# You already know how to check if a list contains an item or not.
# Assume we would like to implement such a function ourselves. Implement a recursive function that, given an element and a list, returns true if the list contains the element and false otherwise.
# It would be a good (and very simple) practice to implement a non-recursive one first.

def find_in_list(n: any, lst: list) -> bool:
    """
    Whether n is present in the given list
    Non-recursive
    """
    return any(item == n for item in lst)


def rec_find_in_list(n: any, lst: list) -> bool:
    """
    Whether n is present in the given list
    Recursive
    """
    if not lst:
        return False

    if lst[0] == n:
        return True

    return rec_find_in_list(n, lst[1:])


def main():
    number = int(input("Number: "))
    nums = list(range(0, 10))

    print(find_in_list(number, nums))
    print(rec_find_in_list(number, nums))


if __name__ == "__main__":
    main()
