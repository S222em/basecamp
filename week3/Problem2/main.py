# There are numerous phrases that are palindromes when spacing is ignored.
# Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others.
# Write a program that ignores spacing while determining whether or not a string is a palindrome
#
# Extra (additional challenge):
# Extend your solution so that is also ignores punctuation marks (like , . ? ! ;)
# Extend your solution so that it treats uppercase and lowercase letters as equivalent.
# Input example:
# Sentence: go dog
# Sentence: some men interpret nine memos
# Sentence: some random sentence
# Output example:
# "go dog" is a palindrome
# "some men interpret nine memos" is a palindrome
# "some random sentence" is not a palindrome
import string

original_sentence = input("Sentence: ")


def should_ignore(char: str):
    return char in string.punctuation or char in string.whitespace


sentence = "".join([char if not should_ignore(char) else "" for char in original_sentence.lower()])
reversed_sentence = sentence[::-1]

print(f"\"{original_sentence}\" is {'' if sentence == reversed_sentence else 'not '}a palindrome")
