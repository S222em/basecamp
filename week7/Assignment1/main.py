# Create a progam that can convert a name/string to the hashed representation of that value.
#
# Menu structure (case insesitive):
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
# Criteria:
# Create a function that given the input string converts it to the encoded/decoded equivalent based on the provided or already set key.
# Make sure to only convert values that are in the key, if the value is not present, use its own value:
#
# encode_string(data: str, key: str = None) -> str:
# decode_string(data: str, key: str = None) -> str:
# Create a function that given a list of inputs converts the complete list to the encoded/decoded equivalent based on the key.
# You can use the already created encode/decode function when looping through the list. Tip! Make use of the map function within Python with a lambda to call the internal function with all elements [element, key] as a return value, you should return a list with the converted values:
#
# encode_list(data: list, key: str = None) -> list:
# decode_list(data: list, key: str = None) -> list:
# Create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct the return value should be a boolean value (True if values match, False if they don't match):
#
# validate_values(encoded: str, decoded: str, key: str = None) -> bool:
# Create a function that given a key, converts to a key (Dict) to be used for converting:
#
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
# set_dict_key(conversion_string: str) -> None:
# Extra:
# For ease of use, you can use the following string as a default key to use within your program:
# a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$
# To test your functions, use the provided unit test file.
# Input example:
# Key: A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@
# E
# PETER
# P
# Q
# Output example:
# >*;*#

DEFAULT_KEY = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"

encode_key_dict = {}
decode_key_dict = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, key: str = None) -> str:
    """
    Encodes any given string using the specified key or a previously specified key
    """
    if key is not None:
        set_dict_key(key)

    encoded = "".join(map(
        lambda char: encode_key_dict[char] if char in encode_key_dict else char,
        data
    ))

    encoded_values.append(encoded)

    return encoded


def decode_string(data: str, key: str = None) -> str:
    """
    Decodes any given string using the specified key or a previously specified key
    """
    if key is not None:
        set_dict_key(key)

    decoded = "".join(map(
        lambda char: decode_key_dict[char] if char in decode_key_dict else char,
        data
    ))

    decoded_values.append(decoded)

    return decoded


def encode_list(data: list, key: str = None) -> list:
    """
    Encodes any given list of strings using the specified key or a previously specified key
    """
    if key is not None:
        set_dict_key(key)

    return [encode_string(item, None) for item in data]


def decode_list(data: list, key: str = None) -> list:
    """
    Decodes any given list of strings using the specified key or a previously specified key
    """
    if key is not None:
        set_dict_key(key)

    return [decode_string(item, None) for item in data]


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    """
    Returns whether the encoded and decoded value match each-other
    given the key or previously specified key
    """
    if key is not None:
        set_dict_key(key)

    return decode_string(encoded, None) == decoded


def set_dict_key(key: str) -> None:
    """
    Creates a dictionary out of the present key that can be used for conversions
    """
    keys = key[0::2]
    values = key[1::2]

    # Global used here is what is expected of this function by codegrade so it can't be removed
    # Would have been better to use a class for all these functions but codegrade does not allow of course
    global encode_key_dict, decode_key_dict
    encode_key_dict = dict(zip(keys, values))
    decode_key_dict = dict(zip(values, keys))


MENU_STRUCTURE = """[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program
"""


def main():
    key = input("Key: ")

    if len(key) % 2 == 1:
        return print("Invalid hashvalue input")

    set_dict_key(key.strip() if key else DEFAULT_KEY)

    while True:
        stop = loop()
        if stop:
            break


def loop():
    menu_selected = input(MENU_STRUCTURE).lower()

    if menu_selected == "e":
        data = input("Data to encode: ")
        print("\n".join(encode_list(data.split(", "), None)))

    if menu_selected == "d":
        data = input("Data to decode: ")
        print("\n".join(decode_list(data.split(", "), None)))

    if menu_selected == "p":
        print("\n".join(encoded_values))
        print("\n".join(decoded_values))

    if menu_selected == "v":
        encoded_data = input("Encoded data: ")
        decoded_data = input("Decoded data: ")

        print(validate_values(encoded_data, decoded_data, None))

    if menu_selected == "q":
        return True


if __name__ == "__main__":
    main()
