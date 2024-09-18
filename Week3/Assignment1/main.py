import re
from typing import Pattern

# Usually companies use predefined templates for their emails.
# A company named XYZ would like to have a Python program that collects basic information and generates an email from a template.
#
# Criteria:
# There are only two templates: Job Offer and Rejection.
# For the Job Offer email, the program asks: first name, last name, job title, annual salary, starting date.
# For the Rejection email, the program asks: first name, last name, job title, with or without feedback, one feedback statement in case it is with feedback.
# First and last names: each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
# The program must check valid input formats: define a function is_name_valid(first_name:str,last_name:str)->bool. The function is_name_valid gets two parameters of type string and returns the result of type boolean.
# Job title: minimum 10 characters without numbers.
# The program must check valid input formats: define a function is_title_valid(title:str)->bool. The function is_title_valid receives one parameter of type string and returns the result of type boolean.
# Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
# The program must check valid input formats: define a function is_salary_valid(salary:str)->bool. The function is_salary_valid receives one parameter of type string and returns the result of type boolean.
# Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
# The program must check valid input formats: define a function is_date_valid(date:str)->bool. The function is_date_valid receives one parameter of type string and returns the result of type boolean.
# Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed (check the example below).
# The program will generate emails until the user answers No to the More Letters? question.
# In case of invalid input from the user, the program must print the message Input error and then repeat the question.
# Sample execution
# Use this sample execution for the templates of the emails.
#
# Input example (Job Offer):
# More Letters? (Yes or No) Yes
# Job Offer or Rejection? Job Offer
# First Name? John
# Last Name? Hartman
# Job Title? Junior Python Programmer
# Annual Salary? 30.500,50
# Start Date?(YYYY-MM-DD) 2021-01-01
# Output example (Job Offer):
# Here is the final letter to send:
# Dear John Hartman,
#  After careful evaluation of your application for the position of Junior Python Programmer,
#  we are glad to offer you the job. Your salary will be 30.500,50 euro annually.
# Your start date will be on 2021-01-01. Please do not hesitate to contact us with any questions.
# Sincerely,
# HR Department of XYZ
# Input example (Rejection):
# More Letters? (Yes or No) Yes
# Job Offer or Rejection? Rejection
# First Name? David
# Last Name? Chan
# Job Title? Software Tester
# Feedback? (Yes or No) Yes
# Enter your Feedback (One Statement): You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.
# Output example (Rejection):
# Here is the final letter to send:
# Dear David Chan,
# After careful evaluation of your application for the position of Software Tester,
# at this moment we have decided to proceed with another candidate.
# Here we would like to provide you our feedback about the interview.
# You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.
# We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.
# Sincerely,
# HR Department of XYZ
# Input example (Exit program):
# More Letters? (Yes or No) No

JOB_OFFER_TEMPLATE = """
Here is the final letter to send:
Dear {} {},
After careful evaluation of your application for the position of {},
we are glad to offer you the job. Your salary will be {} euro annually.
Your start date will be on {}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
"""

REJECTION_TEMPLATE = """
Here is the final letter to send:
Dear {} {},
After careful evaluation of your application for the position of {},
at this moment we have decided to proceed with another candidate.{}
We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
"""

REJECTION_FEEDBACK_TEMPLATE = """
Here we would like to provide you our feedback about the interview.
{}"""

YES_OR_NO_PATTERN = re.compile("(Yes|No)")
TEMPLATE_NAME_PATTERN = re.compile("(Job Offer|Rejection)")
NAME_PATTERN = re.compile("[A-Z}[a-z]{1,9}")
TITLE_PATTERN = re.compile("[^0-9]{10,}")
SALARY_PATTERN = re.compile("([2-7][0-9].[0-9]{3},[0-9]{2})|80\.000,00")
DATE_PATTERN = re.compile("(2021|2022)-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[0-1])")
FEEDBACK_PATTERN = re.compile(".+")


def main():
    while True:
        stop = loop()
        if stop:
            break


def loop() -> bool:
    more = retry_input_until_matches("More Letters? (Yes or No)", YES_OR_NO_PATTERN)
    if more == "No":
        return True

    template = retry_input_until_matches("Job Offer or Rejection?", TEMPLATE_NAME_PATTERN)
    information = get_information_for_template(template)

    if template == "Job Offer":
        print(JOB_OFFER_TEMPLATE.format(*information))
    else:
        print(REJECTION_TEMPLATE.format(*information))


def get_information_for_template(template: str) -> list[str]:
    information = [
        retry_input_until_matches("First Name?", NAME_PATTERN),
        retry_input_until_matches("Last Name?", NAME_PATTERN),
        retry_input_until_matches("Job Title?", TITLE_PATTERN)
    ]

    if template == "Job Offer":
        information += [
            retry_input_until_matches("Annual Salary?", SALARY_PATTERN),
            retry_input_until_matches("Start Date?(YYYY-MM-DD)", DATE_PATTERN)
        ]

    if template == "Rejection":
        if retry_input_until_matches("Feedback? (Yes or No)", YES_OR_NO_PATTERN) == "Yes":
            feedback = retry_input_until_matches("Enter your Feedback (One Statement):", FEEDBACK_PATTERN)
            information.append(REJECTION_FEEDBACK_TEMPLATE.format(feedback))
        else:
            information.append("")

    return information


def retry_input_until_matches(prompt: str, pattern: Pattern[str]) -> str:
    while True:
        user_input = input(f"{prompt} ").strip()
        if pattern.fullmatch(user_input) is not None:
            return user_input

        print("Input error")


if __name__ == "__main__":
    main()
