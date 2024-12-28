# If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching.
# For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them.
# However, if one straw is 6 inches. long, while the other two are each only 2 inches. long, then a triangle cannot be formed.
#
# Criteria:
# Only determin Equilateral triangle
# If any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle
# Use a function called check_triangle(side_a, side_b, side_c) -> bool
# Each side can be on a seperate line
# Print possible on correct triangle and impossible when triangle can't be formed
# Input examples:
# Example 1
#
# Side A: 6
# Side B: 5
# Side C: 4
# Example 2
#
# Side A: 3
# Side B: 1
# Side C: 1
# Output examples:
# Possible triangle
# Impossible triangle

def check_triangle(side_a, side_b, side_c):
    sides = [side_a, side_b, side_c]

    for i, side_i in enumerate(sides):
        sum_of_other_sides = 0
        for j, side_j in enumerate(sides):
            if i == j:
                continue

            sum_of_other_sides += side_j

        if side_i >= sum_of_other_sides:
            return False

    return True


def get_side(name):
    side = input(f"Side {name}: ")

    return int(side)


def main():
    side_a = get_side("A")
    side_b = get_side("B")
    side_c = get_side("C")

    is_possible = check_triangle(side_a, side_b, side_c)

    print("Possible triangle" if is_possible else "Impossible triangle")


if __name__ == "__main__":
    main()
