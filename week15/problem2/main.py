#
# One of the ways to measure the performance of pieces of a code is to measure the time of the execution.
#
# Info:
# For example, the time is recorded at the beginning and at the end of a function.
# Then, the execution time can be calculated.
# A desirable implementation is to not change the body of an already implemented function.
# A decorator can be helpful here. \
#
# Extra:
# Make use of the time import for calculating the difference in time.
#
# Implementation:
# Suppose you have an already implemented function.
# Decorate your function such that its execution time is printed when running it.
import time


def measure(func):
    """
    Returns a wrapper for func that measures it's execution time.
    Prints the result in seconds
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} {end - start}s")

    return inner


@measure
def main():
    # Ridiculous name as apparently just "i" is not good enough anymore?
    i_is_some_random_variable_that_does_not_matter = 1

    for _ in range(1_000_000):
        i_is_some_random_variable_that_does_not_matter += 1


if __name__ == "__main__":
    main()
