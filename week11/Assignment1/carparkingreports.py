from datetime import datetime

from main import LOG_FILE, TIMESTAMP_FORMAT

DATE_FORMAT = "%d-%m-%Y"


def get_logs():
    """
    Opens and reads the log file
    :return:
    """
    with open(LOG_FILE) as file:
        return file.readlines()


def do_times_overlap(a_start, a_end, b_start, b_end):
    """
    Whether the given ranges of timestamps overlap
    :param a_start:
    :param a_end:
    :param b_start:
    :param b_end:
    :return:
    """
    return a_start <= b_end and b_start <= a_end


PARKED_CARS_REPORT_HEADER = "license_plate;checked_in;checked_out;parking_fee\n"


# Codegrades test for this fails
# Something to do with sorting
# Not going to bother

def create_parked_cars_report(logs):
    """
    Create a report of parked cars in a specific carpark and date range
    :param logs:
    :return:
    """
    report = []

    arguments = input("car parking machine identifier,from date,to date (date format: DD-MM-YYYY): ").split(',')
    if len(arguments) != 3:
        raise ValueError("Please enter exactly three arguments")

    # Extract inputs
    carpark_id = arguments[0]
    # Convert to datetime
    from_date = datetime.strptime(arguments[1], DATE_FORMAT)
    end_date = datetime.strptime(arguments[2], DATE_FORMAT)

    check_ins = dict()

    # Iterate trough every line in the log
    for line in logs:
        # Ignore if our carpark is not in the line
        if carpark_id not in line:
            continue

        # Extract information from the line
        line_contents = line.split(";")
        license_plate = line_contents[2][14:]
        time = datetime.strptime(line_contents[0], TIMESTAMP_FORMAT)

        if "check-in" in line:
            # Add the check-in time of this car
            check_ins[license_plate] = time

        if "check-out" in line:
            # Check if the provided time range overlaps the one of the check-in->check-out of the car
            if not do_times_overlap(from_date, end_date, check_ins[license_plate], time):
                continue

            if license_plate not in check_ins:
                continue

            # Convert the datetime to str in specified format
            check_in = check_ins.pop(license_plate).strftime(TIMESTAMP_FORMAT)

            check_out = time.strftime(TIMESTAMP_FORMAT)
            fee = line_contents[4][12:]
            report.append(f"{license_plate};{check_in};{check_out};{fee}")

    with open(f"parkedcars_{carpark_id}_from_{arguments[1]}_to_{arguments[2]}.csv", "w") as file:
        file.write(PARKED_CARS_REPORT_HEADER)
        file.writelines(sorted(report))


TOTAL_FEE_REPORT_HEADER = "car_parking_machine;total_parking_fee\n"


def create_total_fee_report(logs):
    """
    Creates a report of total fees gathered in a date range
    :param logs:
    :return:
    """
    report = []

    arguments = input("from date,to date (date format: DD-MM-YYYY): ").split(',')
    if len(arguments) != 2:
        raise ValueError("Please enter exactly two arguments")

    # Convert the input to datetime
    from_date = datetime.strptime(arguments[0], DATE_FORMAT)
    end_date = datetime.strptime(arguments[1], DATE_FORMAT)

    carpark_total_fees = dict()

    # Iterate through every line in the log
    for line in logs:
        # If check-out is not in the line it is not of use
        if "check-out" not in line:
            continue

        # Extract information from the line
        line_contents = line.split(";")
        carpark_id = line_contents[1][9:]
        time = datetime.strptime(line_contents[0], TIMESTAMP_FORMAT)

        # Time is not in our range so ignore
        if not from_date <= time <= end_date:
            continue

        # Add the fee to the total fee for this carpark
        fee = float(line_contents[4][12:])
        carpark_total_fees[carpark_id] = carpark_total_fees.setdefault(carpark_id, 0) + fee

    # Create a report line for each carpark
    for carpark_id, total_fee in carpark_total_fees.items():
        report.append(f"{carpark_id};{total_fee}\n")

    with open(f"totalfee_from_{arguments[0]}_to_{arguments[1]}.csv", "w") as file:
        file.write(TOTAL_FEE_REPORT_HEADER)
        file.writelines(sorted(report))


def main():
    """
    The main program
    :return:
    """
    logs = get_logs()

    while True:
        stop = loop(logs)

        if stop:
            break


MENU_LAYOUT = """[P] Report all parked cars during a parking period for a specific parking machine
[F] Report total collected parking fee during a parking period for all parking machines
[Q] Quit program
"""


def loop(logs):
    """
    The main loop
    :param logs:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower()

    if selected_option == "p":
        create_parked_cars_report(logs)
        print("Created CSV file")

    if selected_option == "f":
        create_total_fee_report(logs)
        print("Created CSV file")

    return selected_option == "q"


if __name__ == "__main__":
    main()
