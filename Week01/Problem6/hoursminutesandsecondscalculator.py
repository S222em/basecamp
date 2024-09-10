days = input("Days: ")

if not days.isdigit():
    print("Please enter a valid integer")
    exit(0)

days = int(days)

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
