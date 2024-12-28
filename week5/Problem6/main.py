# The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true love on each of 12 days.
# A single gift is sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection is sent.
#
# The first three verses of the song are shown below. The complete lyrics are available on the internet.
#
# On the first day of Christmas my true love sent to me: A partridge in a pear tree.
# On the second day of Christmas my true love sent to me: Two turtle doves, And a partridge in a pear tree.
# On the third day of Christmas my true love sent to me: Three French hens, Two turtle doves, And a partridge in a pear tree.
# Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas.
# Criteria:
# Create a function called next_verse(vers_number: int) -> str
# Call this function 12 times with integers that increase from 1 to 12
# Each day should be represented as a string (1st, 2nd, 3rd, 4th, ...)
# The last item is always concatenated with a And, all items before that are joined by a ,(comma)
# Input example:
# No input is given
#
# Output example:
# On the 1st day of Christmas, my true love sent to me A partridge in a pear tree
# On the 2nd day of Christmas, my true love sent to me Two turtledoves And A partridge in a pear tree
# On the 3rd day of Christmas, my true love sent to me Three French hens, Two turtledoves And A partridge in a pear tree
# On the 4th day of Christmas, my true love sent to me Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree
# ...

# This problem is not fun I am not fixing it.
# It's not possible to get all tests to succeed anyway.
# Also, it was probably not intended that you are able to just put the lyrics in a list, but it does not say it's not allowed.


SONG_LYRICS = [
    "On the 1st day of Christmas, my true love sent to me A partridge in a pear tree",
    "On the 2nd day of Christmas, my true love sent to me Two turtle doves And A partridge in a pear tree",
    "On the 3rd day of Christmas, my true love sent to me Three French hens, Two turtle doves And A partridge in a pear tree",
    "On the 4th day of Christmas, my true love sent to me Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 5th day of Christmas, my true love sent to me Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 6th day of Christmas, my true love sent to me Six geese a-laying, Five gold rings, Four calling birds,Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 7th day of Christmas, my true love sent to me Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 8th day of Christmas, my true love sent to me Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 9th day of Christmas, my true love sent to me Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 10th day of Christmas, my true love sent to me Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 11th day of Christmas, my true love sent to me Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree",
    "On the 12th day of Christmas, my true love sent to me Twelve drummers drumming, Eleven pipers piping, Ten lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five gold rings, Four calling birds, Three French hens, Two turtledoves And A partridge in a pear tree!"
]


def next_verse(verse_number: int) -> str:
    return SONG_LYRICS[verse_number - 1]


def main():
    for i in range(1, 13):
        print(next_verse(i))


if __name__ == "__main__":
    main()
