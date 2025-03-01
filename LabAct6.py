# Define the Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self): # Define the abstract get_info method
        pass

# Define the Electronics class inheriting from Product
class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price) # Call the __init__ method of the parent class
        self.warranty_period = warranty_period

    def get_info(self): # Implement the get_info method for Electronics
        return f"{self.name} | ₱{self.price} | {self.warranty_period} year warranty"

# Define the Clothing class inheriting from Product
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price) # Call the __init__ method of the parent class
        self.size = size

    def get_info(self): # Implement the get_info method for Clothing
        return f"{self.name} | ₱{self.price} | Size: {self.size}"

# Define the ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.cart = []  # Initialize an empty cart
        self.catalog = []  # Initialize an empty catalog

    def add_to_cart(self, product):
        self.cart.append(product)  # Add a product to the cart

    def view_cart(self):
        print("Items in your cart:")
        for product in self.cart:
            print(product.get_info())  # Display information of each product in the cart
        print()

    def checkout(self):
        total = sum(product.price for product in self.cart)  # Calculate the total cost
        print(f"Total cost: ₱{total}")
        confirm = input("Do you want to proceed with the checkout? (yes/no): ") # Confirm checkout
        if confirm.lower() == 'yes': # Proceed with checkout
            print("Checkout successful. Thank you for your purchase!")
        else:
            print("Checkout canceled.")

    def display_catalog(self): # Display the catalog or list of items
        print("Catalog:")
        for i, product in enumerate(self.catalog, start=1):
            print(f"{i}. {product.get_info()}")  # Display each product with its index
        print()

    def add_to_catalog(self, product):
        self.catalog.append(product)  # Add a product to the catalog

def main():
    # Create a ShoppingCart instance
    cart = ShoppingCart()

    # Create Electronics items
    smartphone = Electronics("Smartphone", 84990, 1)
    laptop = Electronics("Laptop", 72990, 1)

    # Create Clothing items
    hoodie = Clothing("Hoodie", 1499, "XL")
    pants = Clothing("Pants", 1199, "L")

    # Add items to the catalog
    cart.add_to_catalog(smartphone)
    cart.add_to_catalog(laptop)
    cart.add_to_catalog(hoodie)
    cart.add_to_catalog(pants)

    while True:
        cart.display_catalog()  # Display the catalog
        print("Menu:")
        print("1. Add to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            item_number = input("Enter the number of the item to add to cart: ")
            if item_number.isdigit(): # Check if the input is a number
                item_number = int(item_number) # Convert the input to an integer
                if 1 <= item_number <= len(cart.catalog): # Check if the number is within the range of items
                    item = cart.catalog[item_number - 1] # Get the item by its number
                    cart.add_to_cart(item) # Add the item to the cart
                    print(f"'{item.name}' has been added to your cart.")
                else:
                    print("Invalid item number.")
            else:
                print("Please enter a valid number.")

        elif choice == "2":
            cart.view_cart()  # View the items in the cart

        elif choice == "3":
            cart.checkout()  # Proceed to checkout

        elif choice == "4": # Exit the program
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")
        print()

if __name__ == "__main__":
    main()