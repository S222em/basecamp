# To keep track of our fincances we want to have a small application.
# We've started with some functionallity but could not figure out the rest.
# Complete the FinanceApp class so it uses the correct queries to return the requested data
#
# To help you, we added the already created functionality so you could reuse it.
# There is also a menu structure within main.py for your ease.
#
# Criteria:
# Use the provided FinanceApp skeleton.
# Fix the load_transactions_from_json method so it loads all data from the provided transactions.json file into the database (Be aware, each year the transactions ID start from 1 again... find a fix for that).
# Each of the following methods already has a return type (as hint) that should be returned, but to help you further the following values should be returned for each method:
#
# FinanceApp:
# add_transaction should return a Transaction object based on the provided arguments and the auto increment id.
# update_transaction should return True if the update succeeded or False if it failed.
# Empty values as argument should be skipped and not used for updating
# delete_transaction should return True if the delete succeeded or False if it failed.
# search_transactions should return a list of objects of type Transaction matching the search term.
# The search term should look for matches inside the category and description of each Transaction.
# get_transactions should return a list of objects of type Transaction matching the provided year, if no year was provided (empty) it should return all transactions.
# get_expenses should return a list of tuples containing the (category and amount) as sum for each category
# This method should only return expenses, so income category='Work' should be ignored.
# Results should be ordered by amount in descending order.
# get_savings should return a list of tuples containing the (year and amount) as sum of savings for each year.
# count_transactions should return an int of the amount of transactions of the provided year, if no year was provided (empty) it should return the total count all transactions.
# get_report should return a dict of the provided year, if no year was provided (empty) it should return the total count all transactions, it should contain the following keys:
# transactions: total count of transactions
# income: total sum of income
# expenses: total sum of expenses
# savings: total sum of savings
# total: total of income, expenses and savings
#
# Output example (A):
# Transaction(999, '2024-12-01', 'Description', 'Test', 1337.00)
# Output example (P):
# Transactions: 999
# Income: 12345.67
# Expenses: -9876.54
# Savings: 1231.23
# Total: -456.78

from app import FinanceApp


def main():
    app = FinanceApp()

    while True:
        print("\nFinance App Menu")
        print("A. Add Transaction")
        print("U. Update Transaction")
        print("D. Delete Transaction")
        print("G. Get Transactions")
        print("S. Search Transactions")
        print("P. Print report")
        print("R. Restore database")
        print("E. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))

            transaction = app.add_transaction(date, description, category, amount)

            print(f"Transaction added: \n{transaction}")

        elif choice == 'U':
            transaction_id = int(input("Enter the transaction ID to update: "))
            date = input("Enter the new date (YYYY-MM-DD): ")
            description = input("Enter the new description: ")
            category = input("Enter the new category: ")
            amount = float(input("Enter the new amount: "))

            if app.update_transaction(transaction_id, date, description, category, amount):
                print("Transaction has been updated")
            else:
                print("Error while updating transaction")

        elif choice == 'D':
            transaction_id = int(input("Enter the transaction ID to delete: "))

            if app.delete_transaction(transaction_id):
                print("Transaction has been deleted")
            else:
                print("Could not delete transaction with id", transaction_id)

        elif choice == 'G':
            year = input("Enter year (leave empty for all): ")

            for transaction in app.get_transactions(year):
                print(transaction)

        elif choice == 'S':
            search_term = input("Search term: ")

            for transaction in app.search_transactions(search_term):
                print(transaction)
        elif choice == 'P':
            year = input("Enter year (leave empty for all): ")

            for key, value in app.get_report(year).items():
                print(f"{key.capitalize()}: {value}")
        elif choice == 'R':
            app.build_database()
            app.load_transactions_from_json('transactions.json')

            print("Database restored")
        elif choice == 'E':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
