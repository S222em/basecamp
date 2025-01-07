# You already know how to implement a Python program that prints positive numbers less than n (non-recursively).
# Implement a recursive function named rec_print(n) that given a positive integer n prints all the positive numbers less than n.

def rec_print(n):
    """
    Prints all integers less than or equal to n in ascending order
    """
    if n < 0:
        return

    rec_print(n - 1)
    print(n)


if __name__ == "__main__":
    rec_print(int(input("Number: ")))
