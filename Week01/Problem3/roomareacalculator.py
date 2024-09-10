width = input("Width: ")
length = input("Length: ")

try:
    width = float(width)
    length = float(length)
    print(f"The Area of the Room: {width * length}")
except ValueError:
    print("Please enter a valid decimal number")
