# Go back to the assignment of week 7.
# Your solution probably relies on a dictionary as a data structure that maps keys to values (to encode / decode a text). \
#
# Suppose you are asked to make your solution more generic, so that if the mapping mechanism / algorithm / structure changes in the future, your implementation for the other functions, mainly encoding and decoding, remain without any changes. For example, in the future, instead of a predefined mapping table, the value for a given key is calculated based on an algorithm. Or a different data structure is used instead of a dictionary. \
#
# Update the encode_string and decode_string functions so that instead of a key, they use a function to do the encoding/decoding with.
# Remember that encode_string and decode_string encode / decode whole strings, not single characters.\
#
# The encode_function should get the data:str as input

hashmap_key_value = {}
encoded_values = []
decoded_values = []


def encode_string(data: str, encode) -> str:
    return encode(data)


def decode_string(data: str, decode) -> str:
    return decode(data)


def encode_list(data: list, encode) -> list:
    return [encode(item) for item in data]


def decode_list(data: list, decode) -> list:
    return [decode(item) for item in data]


def validate_values(encoded: str, decoded: str, encode) -> bool:
    return encode(decoded) == encoded


def main():
    raise NotImplementedError


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
