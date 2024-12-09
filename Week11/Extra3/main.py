import csv


def load_prices(file_name):
    with open(file_name, newline="") as file:
        prices = list(csv.DictReader(file))

    return prices


def get_price_point_for_year(prices, year=2000):
    """
    Returns everything recorded in
    :param prices:
    :param year:
    :return:
    """
    points = []

    for price in prices:
        if str(year) not in price["date"]:
            continue

        points.append(price)

    return points


def main(file_name):
    prices = load_prices(file_name)

    # Hoe ziet het eerste price point eruit?
    price_points = get_price_point_for_year(prices)
    print("Price points: ", *(f"\n{price["name"]}: ${price["dollar_price"]}" for price in price_points))

    # Hoeveel metingen zijn er gedaan?
    print(f"Amount of measurements: {len(prices)}")

    # Wat is de laagste prijs in Amerikaanse dollars van een Big Mac ooit?
    lowest = min(prices, key=lambda price: float(price["dollar_price"]))
    print(f"Lowest ever price in USD: ${lowest["dollar_price"]} in {lowest["name"]}")

    # Wat is de gemiddelde prijs?
    average = sum(float(price["dollar_price"]) for price in prices) / len(prices)
    print(f"Average price: ${average}")

    # In hoeveel landen zijn metingen gedaan?
    countries = set(price["name"] for price in prices)
    print(f"Number of countries that participated: {len(countries)}")

    # In welk land zijn de minste/meeste metingen gedaan?
    measurements_per_country = dict()
    for price in prices:
        measurements_per_country[price["name"]] = measurements_per_country.setdefault(price["name"], 0) + 1

    min_measurements = min(measurements_per_country.items(), key=lambda item: item[1])
    max_measurements = max(measurements_per_country.items(), key=lambda item: item[1])

    print(f"Min measurements is {min_measurements[1]} in {min_measurements[0]}")
    print(f"Max measurements is {max_measurements[1]} in {max_measurements[0]}")

    # Wat is de stijging van de gemiddelde prijs per jaar?
    current_year = None
    sum_of_prices = 0
    amount_of_prices = 0
    averages_per_year = dict()

    for price in prices:
        if current_year != price["date"]:
            if current_year is not None:
                averages_per_year[current_year] = sum_of_prices / amount_of_prices
                sum_of_prices = 0
                amount_of_prices = 0

            current_year = price["date"][:4]

        sum_of_prices += float(price["dollar_price"])
        amount_of_prices += 1

    averages_per_year = list(averages_per_year.items())

    for i, (year, average) in enumerate(averages_per_year[1:]):
        last_year = averages_per_year[i - 1]
        print(f"{year}: {average - last_year[1]}")

    # In welk land is de gemiddelde prijs het meest gestegen?
    start = get_price_point_for_year(prices, year=2000)
    end = get_price_point_for_year(prices, year=2020)
    price_increases_per_country = dict()

    for start_price, end_price in zip(start, end):
        increase = float(end_price["dollar_price"]) - float(start_price["dollar_price"])
        price_increases_per_country[start_price["name"]] = increase

    max_increase = max(price_increases_per_country.items(), key=lambda item: item[1])
    print(f"Max increase was in {max_increase[0]} with ${max_increase[1]}")


if __name__ == "__main__":
    main("big_mac_price.csv")
