# Create a solution for a shop that wants to keep track of the stock of their products and wants to give a discount to customers who buy large quantities of the product.
#
# Write a class called Product
#
# Criteria:
# The class should have attributes called name, amount, and price (holding the product’s name, the number of items of that product in stock, and the regular price of the product).
# There should be a method get_price that receives the number of items to be bought and returns the total costs.
# There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much.
# Extra:
# Regular price if orders have less than 10 item;
# 10% discount is applied for orders of between 10 and 99 items;
# 20% discount is applied for orders of 100 items or more.
# Input example:
# No input is given
#
# Output example:
# No output is required

class Product:
    """
    A product
    """

    def __init__(self, name, amount, price):
        """
        Instantiates a new product
        :param name: The name of the product
        :param amount: The amount of stock for this product
        :param price: The price for this product
        """
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, buy_amount):
        """
        Returns the total price
        Keeps discounts into account
        :param buy_amount: The amount of this product to buy
        :return:
        """
        price = self.price * buy_amount

        if buy_amount < 10:
            return price

        if buy_amount < 100:
            return price * 0.9

        return price * 0.8

    def make_purchase(self, buy_amount):
        """
        Makes the purchase
        Decreases the stock/amount of this product
        :param buy_amount: The amount of this product to buy
        :return:
        """
        self.amount -= buy_amount
