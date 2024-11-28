# Iris is rechercheur en verhoort vaak getuigen van een aanrijding.
# Getuigen omschrijven een auto meestal met de letters en cijfers van de kentekenplaat, bijvoorbeeld AB12CD of 3XYZ45.
# Iris moet die reeksen omzetten in geldige kentekenplaten, bijvoorbeeld AB-12-CD of 3-XYZ-45.
#
# Schrijf een Python-programma dat Iris daarbij helpt.
#
# Voorbeeldinteractie
# -------------------
# Reeks: AB12CD
# AB-12-CD
import string


def convert(series):
    """
    Convert series AB12CD to AB-12-CD
    Does so by adding an - if the previous char is not the same type (alphabetic/numeric)
    :param series:
    :return:
    """
    converted = ""

    for i, char in enumerate(series):
        # If the previous char is not the same type as the current one
        if i != 0 and (char not in string.digits) == (series[i - 1] in string.digits):
            converted += "-"

        converted += char

    return converted


def main():
    series = input("Series: ").upper()

    print(convert(series))


if __name__ == "__main__":
    main()
