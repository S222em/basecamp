# The following data represents average temperatures of the third month for 1995, 2010, and 2020 recorded in Amsterdam.
#
# Dataset:
# temperatures = (
#     ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
#      '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
#     ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
#      '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
#     ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
#      '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
# )
# Criteria:
# Implement a program that given this data prints the answers for the following questions (each seperate line):
#
# How many different values occur as a daily average temperature in both March 1995 and March 2010.
# How many different values occur as a daily average temperature in both March 1995 and March 2020.
# Which year has a day with highest temperature in March?
# Which year had the warmest March?
# Input example:
# No input is given
#
# Output example:
# Answer_1
# Answer_2
# Answer_3
# Answer_4

TEMPERATURES_PER_MONTH = (
    ('1995', '3',
     ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4',
      '40.5',
      '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5',
      '40.5', '47.0']),
    ('2010', '3',
     ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9',
      '42.7',
      '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6',
      '50.1', '43.6']),
    ('2020', '3',
     ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0',
      '48.9',
      '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7',
      '39.5', '40.6'])
)


def parse_temperatures_by_year_month():
    temperatures_by_month = dict()

    for year, month, temperatures in TEMPERATURES_PER_MONTH:
        temperatures_by_month[(year, month)] = [float(temperature) for temperature in temperatures]

    return temperatures_by_month


def filter_temperatures_by_month(temperatures_by_year_month, month):
    filtered_temperatures = dict()

    for year_month, temperatures in temperatures_by_year_month.items():
        if year_month[1] == month:
            filtered_temperatures[year_month] = temperatures

    return filtered_temperatures


def main():
    temperatures = parse_temperatures_by_year_month()

    # How many different values occur as a daily average temperature in both March 1995 and March 2010.
    print(len(set(temperatures[("1995", "3")]).intersection(temperatures[("2010", "3")])))

    # How many different values occur as a daily average temperature in both March 1995 and March 2020.
    print(len(set(temperatures[("1995", "3")]).intersection(temperatures[("2020", "3")])))

    temperatures_march = filter_temperatures_by_month(temperatures, "3")

    # Which year has a day with highest temperature in March?
    max_month_and_year = max(temperatures_march.items(), key=lambda month: max(month[1]))
    print(max_month_and_year[0][0])

    # Which year had the warmest March?
    warmest_month_and_year = max(temperatures_march.items(), key=lambda month: sum(month[1]))
    print(warmest_month_and_year[0][0])


if __name__ == "__main__":
    main()
