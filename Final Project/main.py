from Transaction import Expense, Income, Category

# Main function to run the program
def main():
    categories = {}  # Dictionary to store categories and their transactions
    while True:
        # Display menu options
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Monthly Summary")
        print("4. Filter Transactions by Category")
        print("5. Exit")
        choice = input("Choose an option: ")

        # Handle user choices
        if choice == "1":
            add_transaction(categories)
        elif choice == "2":
            view_transactions(categories)
        elif choice == "3":
            monthly_summary(categories)
        elif choice == "4":
            filter_transactions(categories)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to add a transaction
def add_transaction(categories):
    t_type = input("Enter type (expense/income): ").strip().lower()
    amount = float(input("Enter amount: "))
    category_name = input("Enter category: ").strip()

    # Create a new category if it doesn't exist
    if category_name not in categories:
        categories[category_name] = Category(category_name)

    # Create an Expense or Income object based on the type
    if t_type == "expense":
        transaction = Expense(amount, category_name)
    elif t_type == "income":
        transaction = Income(amount, category_name)
    else:
        print("Invalid transaction type.")
        return

    # Add the transaction to the category
    categories[category_name].add_transaction(transaction)
    print("Transaction added successfully!")

# Function to view all transactions
def view_transactions(categories):
    for category_name, category in categories.items():
        print(f"\nCategory: {category_name}")
        for transaction in category.get_transactions():
            print(transaction.display())

# Function to filter transactions by category
def filter_transactions(categories):
    category_name = input("Enter category to filter by: ").strip()
    if category_name in categories:
        print(f"\nTransactions in category: {category_name}")
        for transaction in categories[category_name].get_transactions():
            print(transaction.display())
    else:
        print("Category not found.")

# Function to display a monthly summary
def monthly_summary(categories):
    total_income = 0  # Total income for the month
    total_expense = 0  # Total expenses for the month

    # Calculate totals by iterating through all transactions
    for category in categories.values():
        for transaction in category.get_transactions():
            if isinstance(transaction, Income):
                total_income += transaction.get_amount()
            elif isinstance(transaction, Expense):
                total_expense += transaction.get_amount()

    # Display the summary
    print("\nMonthly Summary:")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Balance: {total_income - total_expense}")

# Entry point of the program
if __name__ == "__main__":
    main()