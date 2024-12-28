from databasemanager import DatabaseManager


class SalesManager:
    def __init__(self, database_manager: DatabaseManager) -> None:
        self.database = database_manager

    def get_sale(self, sale_id: int) -> tuple:
        """
        Fetches the given id sale id from the database
        :param sale_id:
        :return:
        """
        query = """SELECT * FROM sales WHERE id=?;"""
        parameters = (sale_id,)

        return self.database.fetchone(query, parameters)

    def add_sale(self, date: str, product_id: int, customer_id: int, quantity: int, price: float) -> int:
        """
        Inserts the given sale into the database
        :param date:
        :param product_id:
        :param customer_id:
        :param quantity:
        :param price:
        :return:
        """
        query = """INSERT INTO sales (date, product_id, customer_id, quantity, price) VALUES (?, ?, ?, ?, ?);"""
        parameters = (date, product_id, customer_id, quantity, price)

        return self.database.insert(query, parameters)

    def update_sale(self, sale_id: int, date: str, product_id: int, customer_id: int, quantity: int,
                    price: float) -> bool:
        """
        Updates the given sale id in the database
        :param sale_id:
        :param date:
        :param product_id:
        :param customer_id:
        :param quantity:
        :param price:
        :return:
        """
        query = """UPDATE sales SET date=?, product_id=?, customer_id=?, quantity=?, price=?
                    WHERE id=?;"""
        parameters = (date, product_id, customer_id, quantity, price, sale_id)

        return self.database.update(query, parameters)

    def delete_sale(self, sale_id: int) -> bool:
        """
        Deletes the given sale id
        :param sale_id:
        :return:
        """
        query = """DELETE FROM sales WHERE id=?;"""
        parameters = (sale_id,)

        return self.database.delete(query, parameters)

    def get_customer(self, customer_id: int) -> tuple:
        """
        Fetches the given customer from the database
        :param customer_id:
        :return:
        """
        query = """SELECT * FROM customers WHERE id=?;"""
        parameters = (customer_id,)

        return self.database.fetchone(query, parameters)

    def add_customer(self, name: str, email: str) -> int:
        """
        Creates a new customer
        :param name:
        :param email:
        :return:
        """
        query = """INSERT INTO customers (name, email) VALUES (?, ?);"""
        parameters = (name, email)

        return self.database.insert(query, parameters)

    def update_customer(self, customer_id: int, name: str, email: str) -> bool:
        """
        Updates a customer
        :param customer_id:
        :param name:
        :param email:
        :return:
        """
        query = """UPDATE customers SET name=?, email=? WHERE id=?"""
        parameters = (name, email, customer_id)

        return self.database.update(query, parameters)

    def delete_customer(self, customer_id: int) -> bool:
        """
        Deletes a customer
        :param customer_id:
        :return:
        """
        query = """DELETE FROM customers WHERE id=?"""
        parameters = (customer_id,)

        return self.database.delete(query, parameters)

    def get_product(self, product_id: int) -> tuple:
        """
        Fetches a product
        :param product_id:
        :return:
        """
        query = """SELECT * FROM products WHERE id=?;"""
        parameters = (product_id,)

        return self.database.fetchone(query, parameters)

    def add_product(self, name: str, category: str) -> int:
        """
        Adds a product to the database
        :param name:
        :param category:
        :return:
        """
        query = """INSERT INTO products (name, category) VALUES (?, ?);"""
        parameters = (name, category)

        return self.database.insert(query, parameters)

    def update_product(self, product_id: int, name: str, category: str) -> bool:
        """
        Updates a product in the database
        :param product_id:
        :param name:
        :param category:
        :return:
        """
        query = """UPDATE products SET name=?, category=? WHERE id=?"""
        parameters = (name, category, product_id)

        return self.database.update(query, parameters)

    def delete_product(self, product_id: int) -> bool:
        """
        Deletes a product in the database
        :param product_id:
        :return:
        """
        query = """DELETE FROM products WHERE id=?"""
        parameters = (product_id,)

        return self.database.delete(query, parameters)
