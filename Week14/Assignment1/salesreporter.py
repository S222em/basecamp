from databasemanager import DatabaseManager


class SalesReporter:
    def __init__(self, database_manager: DatabaseManager) -> None:
        self.database = database_manager

    def sales_amount(self) -> int:
        """
        The amount of sales that have been made
        :return:
        """
        query = """SELECT COUNT(*) FROM sales;"""

        return self.database.fetchone(query)[0]

    def total_sales(self) -> float:
        """
        The total amount of sales that has been made
        :return:
        """
        query = """SELECT ROUND(SUM(quantity * price), 2) FROM sales;"""

        return self.database.fetchone(query)[0]

    def sales_by_product(self) -> str:
        """
        Returns a formatted table containing the total number of a product sold and the total price
        :return:
        """
        query = """SELECT products.name, SUM(sales.quantity), ROUND(SUM(sales.quantity * sales.price), 2) FROM sales
                    INNER JOIN products ON sales.product_id = products.id
                    GROUP BY products.id;"""

        headers = ["Product", "Quantity", "Sales"]
        rows = self.database.fetchall(query)

        return self.display_table(headers, rows)

    def sales_by_customer(self) -> str:
        """
        Returns the total quantity and amount a customer has bought in a table
        :return:
        """
        query = """SELECT customers.name, SUM(sales.quantity), ROUND(SUM(sales.quantity * sales.price), 2) FROM sales
                    INNER JOIN customers ON sales.customer_id = customers.id
                    GROUP BY customers.id;"""

        headers = ["Customer", "Quantity", "Sales"]
        rows = self.database.fetchall(query)

        return self.display_table(headers, rows)

    def sales_over_time(self) -> str:
        """
        Returns the amount of sales at each date
        :return:
        """
        query = """SELECT date, ROUND(SUM(quantity * price), 2) FROM sales GROUP BY date;"""

        headers = ["Date", "Sales"]
        rows = self.database.fetchall(query)

        return self.display_table(headers, rows)

    def top_selling_products(self, amount: int = 5) -> str:
        """
        Returns x amount of best-selling products
        :param amount:
        :return:
        """
        query = """SELECT products.name, SUM(sales.quantity) FROM sales
                    INNER JOIN products ON sales.product_id = products.id
                    GROUP BY sales.product_id
                    ORDER BY SUM(sales.quantity) DESC;"""

        headers = ["Product", "Quantity"]
        rows = self.database.fetchall(query)

        return self.display_table(headers, rows[:amount])

    def top_customers(self, amount: int = 5) -> str:
        """
        Returns x amount of top customers
        :param amount:
        :return:
        """
        query = """SELECT customers.name, ROUND(SUM(sales.quantity * sales.price), 2) FROM sales
                    INNER JOIN customers ON sales.customer_id = customers.id
                    GROUP BY sales.customer_id
                    ORDER BY SUM(sales.quantity * sales.price) DESC;"""

        headers = ["Customer", "Sales"]
        rows = self.database.fetchall(query)

        return self.display_table(headers, rows[:amount])

    def display_table(self, headers: list[str], rows: list[tuple]) -> str:
        """
        Formats and displays a list of rows as a table with headers.

        Parameters:
        headers (list of str): The column headers of the table.
        rows (list of tuple): The data rows to be displayed in the table. Each tuple represents a row of data.

        Returns:
        str: A string representation of the table formatted for display.

        Example:
        >>> headers = ["Product", "Total Quantity", "Total Sales"]
        >>> rows = [("Product A", 100, 999.99), ("Product B", 150, 1499.99), ("Product C", 200, 1999.99)]
        >>> reporter = SalesReporter('sales.db')
        >>> table_str = reporter.display_table(headers, rows)
        >>> print(table_str)

        Example Output:
        Product   | Total Quantity | Total Sales
        ---------+----------------+------------
        Product A | 100            | 999.99
        Product B | 150            | 1499.99
        Product C | 200            | 1999.99
        """
        column_widths: list = [max(len(str(item)) for item in column) for column in zip(*([headers] + rows))]
        row_format: str = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        table: list = list()

        table.append(row_format.format(*headers))
        table.append("-+-".join(['-' * width for width in column_widths]))

        for row in rows:
            table.append(row_format.format(*row))

        return "\n".join(table)
