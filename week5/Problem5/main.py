# Coming up with new random passwords is becoming a hard task.
# To make this job a lot easier, you are going to implement a program that creates a random password.
#
# Criteria:
# Create a function called generate_random_password() -> str
# The password should have a random length of between 7 and 10 characters
# Each character should be randomly selected from positions 33 to 126 in the ASCII table
# Input example:
# No input is given
#
# Output example:
# Zo9o3fA2
from random import randint


def generate_random_password() -> str:
    length = randint(7, 10)

    return "".join(chr(randint(33, 126)) for _ in range(length))


def main():
    password = generate_random_password()

    print(password)


if __name__ == "__main__":
    main()
