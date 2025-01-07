# Implement two functions, one for non-recursive and one recursive, that calculate the result of multiplication of positive numbers less than or equal given n.
# For example, given n=5, the result will be 120 (because 5*4*3*2*1=120).
# Note: In mathematics this is called calculating n-factorial.


def factorial(n):
    """
    Calculates the factorial of n without recursion
    """
    # This would have been ideal but of course I cant import reduce or mul....
    # return reduce(mul, range(1, n + 1), 1)

    total = 1

    for i in range(1, n + 1):
        total *= i

    return total


def rec_factorial(n):
    """
    Calculates the factorial of n with recursion
    """
    if n == 0:
        return 1

    return n * rec_factorial(n - 1)


def main():
    number = int(input("Number: "))

    print(factorial(number))
    print(rec_factorial(number))


if __name__ == "__main__":
    main()
