# A string is a palindrome if it is identical forward and backward.
# For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.
# Write a program that reads a string from the user and uses a loop to determines whether it is a palindrome.
# Display the result, including a meaningful output message.
#
# Extra (additional challenge):
# Extend your solution so that is also ignores punctuation marks (like , . ? ! ;)
# Extend your solution so that it treats uppercase and lowercase letters as equivalent.
# Input example:
# String: anna
# String: hannah
# String: lepels
# Output example:
# "anna" is a palindrome
# "hannah" is a palindrome
# "lepels" is not a palindrome
import string

word = input("String: ").lower()

is_palindrome = True

i = 0
j = len(word) - 1

while i < j:
    if word[i] in string.punctuation:
        i += 1

    if word[j] in string.punctuation:
        j -= 1

    if word[i] != word[j]:
        is_palindrome = False
        break

    i += 1
    j -= 1

print(f"\"{word}\" is {'' if is_palindrome else 'not '}a palindrome")
