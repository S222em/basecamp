# An online retailer sells two products: widgets and gizmos.
# Write a program that reads the number of widgets and the number of gizmos in an order from the user.
# Then your program should compute and display the total weight of the order.
#
# Criteria:
# Each widget weighs 75 grams
# Each gizmo weighs 112 grams
# Input example:
# Number of widgets: 10
# Number of gizmos: 1
#
# Output example:
# The Total Weight of the Order: 862 grams

WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112


def validate_and_convert_to_int(to_convert: str):
    if not to_convert.isdigit():
        print("Please enter a valid integer")
        exit()

    return int(to_convert)


widgets = validate_and_convert_to_int(input("Number of widgets: "))
gizmos = validate_and_convert_to_int(input("Number of gizmos: "))

total = widgets * WIDGET_WEIGHT + gizmos * GIZMO_WEIGHT

print(f"The Total Weight of the Order: {total} grams")
