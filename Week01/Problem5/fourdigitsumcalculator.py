numbers_str = input()

if not numbers_str.isdigit():
    print("Please enter a valid integer")
    exit(0)

numbers = [int(number) for number in numbers_str]

total_sum = sum(numbers)

print(f"{'+'.join([str(number) for number in numbers])}={total_sum}")
