# A primary school teacher needs to automate basic arithmetic (summation, multiplication table, subtraction) exercises for her students.
# You are asked to implement a program that asks what type of the arithmetic the user needs to practice.
# Then, the program will generate exercises and the user should give the result.
#
# Criteria:
# For each arithmetic operation keep the total number of the exercises 10
# The program must be interactive (generate random numbers for each operation, use random module)
# Your program must be implemented with a function arithmetic_operation(arithmetic_type)
# The artihmetic_type can be (summation, multiplication, subtraction)
# Numbers for summation, subtractions and multiplications will be between 1 and 100
# Collect all the mistakes from the user and print them at the end
# Input example:
# Arethmetic operation: summation
# 1 + 4 = 4
# 3 + 3 = 6
# 6 + 2 = 8
# 5 + 1 = 7
# 3 + 8 = 8
# 5 + 4 = 9
# 8 + 3 = 10
# 1 + 6 = 7
# 3 + 9 = 11
# Output example:
# You had 4 correct and 6 incorrect answers in "summation"
import random

AMOUNT_OF_QUESTIONS = 10

OPERATION_TYPES = {"summation": "+", "multiplication": "*", "subtraction": "-"}


def get_operation_type():
    while True:
        operation_type = input("Arithmetic operation (summation/multiplication/subtraction): ")

        if operation_type in OPERATION_TYPES:
            return operation_type

        print("Please enter one of: summation/multiplication/subtraction")


def get_user_answer(question):
    while True:
        answer = input(f"{question} = ")

        if answer.isdigit():
            return int(answer)

        print("Please enter a valid number")


def get_correct_answer(left, right, operator):
    if operator == "+":
        return left + right

    if operator == "*":
        return left * right

    return left - right


def arithmetic_operation(operator):
    left = random.randint(1, 100)
    right = random.randint(1, 100)
    # As eval is not allowed
    correct_answer = get_correct_answer(left, right, operator)

    question = f"{left} {operator} {right}"
    user_answer = get_user_answer(question)

    return correct_answer == user_answer


def main():
    operation_type = get_operation_type()
    operator = OPERATION_TYPES[operation_type]

    correct = 0

    for _ in range(AMOUNT_OF_QUESTIONS):
        is_user_correct = arithmetic_operation(operator)

        if is_user_correct:
            correct += 1

    incorrect = AMOUNT_OF_QUESTIONS - correct

    print(f"You had {correct} correct and {incorrect} incorrect answers in \"{operation_type}\"")


if __name__ == "__main__":
    main()
