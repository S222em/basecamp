# Morse Code Translator: Morse code is an encoding scheme that uses dashes and dots to represent numbers and letters. Implement a program that uses a dictionary to store the mapping from letters and numbers to Morse code.
#
# Criteria:
# Your program should read a message from the user. Then it should translate each character in the message to its mapping code (function-name: message_to_morse).
# Put a space between translated character. Example: Hello is translated into .... . .-.. .-.. ---
# Put a 4 spaces when there is a space in the original message. Example: Hello World is translated into .... . .-.. .-.. ---    .-- --- .-. .-.. -...
# Your program should print the error message Can't convert char [X] if there is no mapping for specific characters. (where X is the character that is not found)
# Extend your program with functionality of decoding a morse code (function-name: morse_to_message).
# Extend your program with a function translate_text such that given a string it detects if it is a normal text or a morse code. Then based on the type of the message it translates to the other one.
# Input examples:
# Hello
# Hello World
# Output examples:
# .... . .-.. .-.. ---
# .... . .-.. .-.. ---    .-- --- .-. .-.. -...

CHAR_TO_MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    " ": "  "
}

# Switches key and values of CHAR_TO_MORSE, char s represents a space.
MORSE_TO_CHAR = dict(zip(CHAR_TO_MORSE.values(), CHAR_TO_MORSE.keys()), s=" ")

CONVERT_ERROR_MESSAGE = "Can't convert char [{}]"


def message_to_morse(message: str) -> str:
    morse = ""

    for char in message.strip().lower():
        if char not in CHAR_TO_MORSE:
            return CONVERT_ERROR_MESSAGE.format(char)

        morse += f"{CHAR_TO_MORSE[char]} "

    return morse


def morse_to_message(morse: str) -> str:
    message = ""

    # Replace spaces with the character "s" so it can be converted easily
    morse_chars = morse.strip().replace("    ", " s ").split(" ")

    for morse_char in morse_chars:
        if morse_char not in MORSE_TO_CHAR:
            return CONVERT_ERROR_MESSAGE.format(morse_char)

        message += MORSE_TO_CHAR[morse_char]

    return message


def translate_text(text: str) -> str:
    if all(char in "-. " for char in text):
        return morse_to_message(text)

    return message_to_morse(text)


def main():
    text_containing_anything_as_text_is_not_clear_enough_apparently = input("Text: ")

    print(translate_text(text_containing_anything_as_text_is_not_clear_enough_apparently))


if __name__ == "__main__":
    main()
