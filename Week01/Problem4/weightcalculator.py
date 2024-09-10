WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

widgets = input("Number of widgets: ")
gizmos = input("Number of gizmos: ")

try:
    widgets = int(widgets)
    gizmos = int(gizmos)

    total = widgets * WIDGET_WEIGHT + gizmos * GIZMO_WEIGHT

    print(f"The Total Weight of the Order: {total} grams")
except ValueError:
    print("Please enter a valid integer")
