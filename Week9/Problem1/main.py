# Create an application for a car dealer.
#
# The problem is split up into three steps to help you set up a proper structure for the application.
#
# Step 1 - Create a class name Car:
# Criteria:
# Create four fields (brand, model, color, price) and implement these using the init function.
# Create a fifth field called sold. The default value for sold is False.
# Create a method called sell that changes the value of sold to True.
# Create a method called print that prints all fields in a comprehensible way (see example).
# Output example (print):
# Brand: BMW
# Model: X5
# Color: Black
# Price: 34.899
# Not sold yet
#
# Step 2 - Create a new class named Customer:
# Criteria:
# Give it one field (name) and properly implement it.
# Create a method print that returns all fields in a comprehensible way (see example).
# Modify the Car class with a field sold_to, set this field to an object of Customer within the sell method
# (which now needs a parameter with a Customer object).
# Edit the print method of the Car to print the information about the customer if the car has been sold, in addition to the information that will already be printed.
# Adjust other code where needed to get everything working properly.
# Output example (print - Customer):
# Name: John Doe
# Output example (print - Car):
# Brand: BMW
# Model: X5
# Color: Black
# Price: 34.899
# Sold to: John Doe
#
# Step 3 - Extending business by selling motorcycles:
# Write all code to properly introduce this into the existing application.

class Vehicle:
    def __init__(self, brand, model, color, price, sold=False):
        """
        Instantiates a new vehicle
        :param brand: The brand of the vehicle
        :param model: The model of the vehicle
        :param color: The color of the vehicle
        :param price: The price of the vehicle
        :param sold: Whether the vehicle is sold, defaults to False
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = sold
        self.sold_to = None

    def sell(self, customer):
        """
        Sells the vehicle to a customer
        :param customer: The customer to sell to
        :return:
        """
        self.sold = True
        self.sold_to = customer

    def print(self):
        """
        Print information about this vehicle
        :return:
        """
        print(
            f"Brand: {self.brand}",
            f"\nModel: {self.model}",
            f"\nColor: {self.color}",
            f"\nPrice: {self.price}",
            f"\n{self.sold_to.name if self.sold else 'Not sold yet'}"
        )


class Car(Vehicle):
    """
    A car
    """
    pass


class Motorcycle(Vehicle):
    """
    A motorcycle
    """
    pass


class Customer:
    """
    A customer
    """

    def __init__(self, name):
        """
        Instantiate a new customer
        :param name:
        """
        self.name = name

    def print(self):
        """
        Print information about this customer
        :return:
        """
        print(f"Name: {self.name}")


if __name__ == "__main__":
    # Simple test, not sure what else to put here
    car = Car("BMW", "X5", "Black", 34.899)
    car.print()
