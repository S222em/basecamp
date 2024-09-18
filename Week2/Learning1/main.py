def main():
    # Convert decimal number 45 to binary
    print(bin(45))

    # Convert binary number 1010101 to decimal
    print(int("1010101", 2))

    # Add binary numbers 10111 and 1101 together and express in binary
    print(bin(0b10111 + 0b1101))

    # Convert decimal number 255 to hexadecimal
    print(hex(255))

    # Convert hexadecimal number 2a to decimal
    print(0x2a)

    # Add hexadecimal numbers c4 and 3a together and express in hexadecimal
    print(hex(0xc4 + 0x3a))

    # Convert binary number 1101 to decimal
    print(0b1101)

    # Convert hexadecimal number f0 to decimal
    print(0xf0)

    # Add decimal numbers 123 and 456 and express in decimal
    print(123 + 456)

    # Convert decimal number 157 to binary and then to hexadecimal
    print(hex(int(bin(157), 2)))

    # Convert binary number 11101101 to decimal and then to hexadecimal
    print(hex(int("11101101", 2)))

    # Convert hexadecimal number ab4 to decimal and then to binary
    print(bin(int("ab4", 16)))


if __name__ == "__main__":
    main()
