# In an application a valid password must be a combination of digits, uppercase and lowercase letters  and only four symbols * @ ! ?.
# Implement a Python program that asks the password of the user and checks if it is a valid password.
#
# Criteria:
# The length of the password must not be less than 8 characters and must not be more than 20 characters.
# In case the password is not valid, the user can try maximum three times to validate the password.
# Print Valid on a validated password and Invalid on a unvalidated password.
# Use sets and set operations to solve this problem.
# Input example:
# Password: B4s3c4p
#
# Output example:
# Password is invalid

# As importing string module is not allowed
PASSWORD_PATTERNS = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789", "*@!?"]


def is_password_valid(password) -> bool:
    if len(password) < 8 or len(password) > 20:
        return False

    password_patterns = set()

    for char in password:
        in_pattern = False
        for pattern in PASSWORD_PATTERNS:
            if char in pattern:
                password_patterns.update({pattern})
                in_pattern = True
                break

        if not in_pattern:
            return False

    return len(password_patterns) == len(PASSWORD_PATTERNS)


def loop():
    password = input("Password: ")
    password_valid = is_password_valid(password)

    print("Password is valid" if password_valid else "Password is invalid")

    return password_valid


def main():
    attempts = 0

    while True:
        password_valid = loop()

        if password_valid:
            break

        attempts += 1

        if attempts == 4:
            break


if __name__ == "__main__":
    main()
