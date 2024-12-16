from datetime import datetime

from Assignment1.main import connect, adapt_datetime_iso

DATE_FORMAT = "%d-%m-%Y"


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


def create_parked_cars_report(connection):
    """
    Create a report of parked cars in a specific carpark and date range
    :param connection:
    :return:
    """
    report = []

    arguments = input("car parking machine identifier,from date,to date (date format: DD-MM-YYYY): ").split(',')

    car_parking_machine = arguments[0]
    start_date = datetime.strptime(arguments[1], DATE_FORMAT)
    end_date = datetime.strptime(arguments[2], DATE_FORMAT)

    query = """SELECT license_plate, check_in AS "check_in [DATETIME]", check_out AS "check_out [DATETIME]", parking_fee FROM parkings 
                WHERE car_parking_machine=? AND check_out IS NOT NULL"""
    parameters = (car_parking_machine,)

    cursor = connection.execute(query, parameters)
    rows = cursor.fetchall()

    rows_sorted_by_check_in = sorted(rows, key=lambda row: row[1], reverse=True)

    for row in rows_sorted_by_check_in:
        if not do_times_overlap(row[1], row[2], start_date, end_date):
            continue

        check_in = adapt_datetime_iso(row[1])
        check_out = adapt_datetime_iso(row[2])

        report.append(f"{row[0]};{check_in};{check_out};{row[3]}\n")

    with open(f"parkedcars_{car_parking_machine}_from_{arguments[1]}_to_{arguments[2]}.csv", "w") as file:
        file.write(PARKED_CARS_REPORT_HEADER)
        file.writelines(report)


TOTAL_FEE_REPORT_HEADER = "car_parking_machine;total_parking_fee\n"


def create_total_fee_report(connection):
    """
    Creates a report of total fees gathered in a date range
    :param connection:
    :return:
    """
    report = []

    arguments = input("from date,to date (date format: DD-MM-YYYY): ").split(',')

    start_date = datetime.strptime(arguments[0], DATE_FORMAT)
    end_date = datetime.strptime(arguments[1], DATE_FORMAT)

    query = """SELECT car_parking_machine, check_in AS "check_in [DATETIME]", check_out AS "check_out [DATETIME]", parking_fee FROM parkings 
                WHERE check_out IS NOT NULL"""

    cursor = connection.execute(query)
    rows = cursor.fetchall()

    total_fee = dict()

    for row in rows:
        if not do_times_overlap(row[1], row[2], start_date, end_date):
            continue

        total_fee[row[0]] = total_fee.setdefault(row[0], 0) + row[3]

    for car_parking_machine, total_fee in total_fee.items():
        report.append(f"{car_parking_machine};{total_fee}\n")

    with open(f"totalfee_from_{arguments[0]}_to_{arguments[1]}.csv", "w") as file:
        file.write(TOTAL_FEE_REPORT_HEADER)
        file.writelines(report)


CAR_REPORT_HEADER = "car_parking_machine;check_in;check_out;parking_fee\n"


def create_car_report(connection):
    """
    Creates a report of all the carparks the car has parked in
    :param connection:
    :return:
    """
    report = []

    license_plate = input("License plate: ")

    query = """SELECT car_parking_machine, check_in AS "check_in [DATETIME]", check_out AS "check_out [DATETIME]", parking_fee FROM parkings
                WHERE license_plate=? AND check_out IS NOT NULL"""
    parameters = (license_plate,)

    cursor = connection.execute(query, parameters)
    rows = cursor.fetchall()

    rows_sorted_by_check_in = sorted(rows, key=lambda row: row[1], reverse=True)

    for row in rows_sorted_by_check_in:
        check_in = adapt_datetime_iso(row[1])
        check_out = adapt_datetime_iso(row[2])

        report.append(f"{row[0]};{check_in};{check_out};{row[3]}\n")

    with open(f"all_parkings_for_{license_plate}.csv", "w") as file:
        file.write(CAR_REPORT_HEADER)
        file.writelines(report)


def main():
    """
    The main program
    :return:
    """
    connection = connect()

    while True:
        stop = loop(connection)

        if stop:
            break


MENU_LAYOUT = """[P] Report all parked cars during a parking period for a specific parking machine
[F] Report total collected parking fee during a parking period for all parking machines
[C] Report all complete parkings over all parking machines for a specific car
[Q] Quit program
"""


def loop(connection):
    """
    The main loop
    :param connection:
    :return:
    """
    selected_option = input(MENU_LAYOUT).lower()

    if selected_option == "p":
        create_parked_cars_report(connection)
        print("Created CSV file")

    if selected_option == "f":
        create_total_fee_report(connection)
        print("Created CSV file")

    if selected_option == "c":
        create_car_report(connection)
        print("Created CSV file")

    return selected_option == "q"


if __name__ == "__main__":
    main()
