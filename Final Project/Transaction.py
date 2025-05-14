# Base class for all transactions
class Transaction:
    def __init__(self, amount, category):
        # Private attributes with two decimal places
        self._amount = round(amount, 2)
        self._category = category

    # Abstract method to be implemented by subclasses
    def display(self):
        print("Subclasses must implement this method")

    # Getter for the amount
    def get_amount(self):
        return self._amount

    # Setter for the amount with rounding to two decimal places
    def set_amount(self, amount):
        self._amount = round(amount, 2)


# Derived class for expenses
class Expense(Transaction):
    # Override display method for expenses
    def display(self):
        return f"Expense: P{self._amount} in {self._category}"


# Derived class for incomes
class Income(Transaction):
    # Override display method for incomes
    def display(self):
        return f"Income: P{self._amount} from {self._category}"


# Class to manage categories and their transactions
class Category:
    def __init__(self, name):
        self.name = name  # Name of the category
        self.transactions = []  # List to store transactions

    # Add a transaction to the category
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # Retrieve all transactions in the category
    def get_transactions(self):
        return self.transactions