ITEMS = {
    "Jongbelegen kaas": 299,
    "Appeltaart": 549,
    "Melk": 199,
    "Pacifistische Wilde Zalm": 1099
}

"""
Maak een eenvoudig bonnen print systeem voor een supermarkt
De BTW is 21% (alle prijzen hierboven zijn inclusief BTW)

Print de bon op de volgende manier:

Omschrijving prijs btw
Omschrijving prijs btw
----------------------
Totaal: prijs btw
"""


def format_line(name: str, price: int, tax: float) -> str:
    return f"{f'{name[0:13]}{'..' if len(name) > 15 else ''}':<15} €{price / 100:<6.2f} €{tax / 100:.2f}btw\n"


def main():
    receipt = ""
    total_price = 0

    for name, price in ITEMS.items():
        tax = price / 1.21 * 0.21
        receipt += format_line(name, price, tax)
        total_price += price

    total_tax = total_price / 1.21 * 0.21
    receipt += f"----------------------------------\n{'Totaal:':<15} €{total_price / 100:<6.2f} €{total_tax / 100:.2f}btw"

    print(receipt)


if __name__ == "__main__":
    main()
