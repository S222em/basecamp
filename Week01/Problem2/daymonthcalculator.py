years = input("Years: ")

if not years.isdigit():
    print("Please enter a valid integer number")
    exit(0)

years = int(years)

months = years * 12
days = years * 365

print(f"Months: {months}, Days: {days}")
