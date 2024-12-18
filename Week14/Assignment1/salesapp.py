from databasemanager import DatabaseManager
from salesmanager import SalesManager
from salesreporter import SalesReporter

# During a power outage a piece of our sales software got corrupted.
# Luckily we had a backup.json that we can use for our data, but our SalesManager and SalesReporter classes had to be restored to a prior date. Sadly these classes are now missing an implementation, it's your task to fix this.
#
# Criteria:
# Use the provided DatabaseManager for communication, this will help you write less code, it also provides functionality for restoring the backup.
# The salesapp.py file is provided with testing boilerplate, use it to your convenience.
# Do not alter or create any tables, the restore_from_json method in the DatabaseManager will do this for you (just call it).
# All numbers representing money (sales or total of sales) should be rounded to 2 decimals.
# SalesManager
# This class provides basic methods for getting, adding, updating and deleting a customer, product or sale.
# The implementation was corrupted, so you need to fix this, create the queries based on the given parameters for that method.
#
# SalesReporter
# This class is also corrupted and needs to be fixed. \
#
# sales_amount should return the amount of sales made as int
# total_sales should return the total sum of all sales combined as float
# We've managed to implement a display_table method for returning some data in a structured table format.
# The following methods will return an table via display_table as return value (str):
#
# sales_by_product should return a table containing the following info per product (group) ["Product", "Quantity", "Sales"]
# sales_by_customer should return a table containing the following info per customer (group) ["Customer", "Quantity", "Sales"]
# sales_over_time should return a table containing the following info per date (group) ["Date", "Sales"]
# top_selling_products should return a table containing the following info per product (group) [Product", "Quantity"]
# top_customers should return a table containing the following info per customer (group) ["Customer", "Sales ]
# Output example (top_customers):
# Customer    | Sales
# ------------+-------
# John Doe    | 981.00
# ....
# the return value is piped via self.display_table(headers, rows)

if __name__ == "__main__":
    databasemanager: DatabaseManager = DatabaseManager(':memory:')
    databasemanager.restore_from_json('backup.json')

    salesreporter: SalesReporter = SalesReporter(databasemanager)
    salesmanager: SalesManager = SalesManager(databasemanager)

    print("Sales Amount:")
    print(salesreporter.sales_amount(), "\n")
    print("Total Sales:")
    print(salesreporter.total_sales(), "\n")
    print("Sales by Product:")
    print(salesreporter.sales_by_product(), "\n")
    print("Sales by Customer:")
    print(salesreporter.sales_by_customer(), "\n")
    print("Sales Over Time:")
    print(salesreporter.sales_over_time(), "\n")
    print("Top Selling Products:")
    print(salesreporter.top_selling_products(), "\n")
    print("Top Customers:")
    print(salesreporter.top_customers(), "\n")

    # Create + Update + Delete Customer
    customer_id = salesmanager.add_customer('New Customer', 'newcustomer@example.com')
    assert customer_id > 0
    assert salesmanager.update_customer(customer_id, 'Jane Doe', 'jane@doe.com')
    assert salesmanager.get_customer(customer_id) == (customer_id, 'Jane Doe', 'jane@doe.com')
    assert salesmanager.delete_customer(customer_id)
    assert not salesmanager.get_customer(customer_id)

    # Create + Update + Delete Product
    product_id = salesmanager.add_product('New Product', 'Category X')
    assert product_id > 0
    assert salesmanager.update_product(product_id, 'Basecamp Gear', 'Climbing')
    assert salesmanager.get_product(product_id) == (product_id, 'Basecamp Gear', 'Climbing')
    assert salesmanager.delete_product(product_id)
    assert not salesmanager.get_product(product_id)

    # Create + Update + Delete Sale
    sale_id = salesmanager.add_sale('2022-02-02', 1, 1, 1, 100)
    assert sale_id > 0
    assert salesmanager.update_sale(sale_id, '2024-02-01', product_id, customer_id, 5, 9.99)
    assert salesmanager.get_sale(sale_id)[1] == '2024-02-01'
    assert salesmanager.get_sale(sale_id)[4] == 5
    assert salesmanager.delete_sale(sale_id)
    assert not salesmanager.get_sale(sale_id)

    databasemanager.close()
