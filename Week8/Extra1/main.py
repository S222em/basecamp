def successive_numbers(numbers: list[int]):
    i = 0
    j = 1

    while i != len(numbers) and j != len(numbers):
        sum_of = sum(numbers[i:j])

        if sum_of == 10:
            return numbers[i:j]

        if sum_of > 10:
            i += 1
        else:
            j += 1


def main():
    numbers = [-11, 1, 20, -11, -11]

    print(successive_numbers(numbers))


if __name__ == "__main__":
    main()
