# Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Book is available by default

    def borrow_book(self):
        if self.is_available:
            self.is_available = False  # Update availability to False when borrowed
            return True
        return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True  # Update availability to True when returned
            return True
        return False

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} - {status}"  # String representation of the book e.g. "The Great Gatsby - Available"


# Define the Library class
class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list of books

    def add_book(self, book):
        self.books.append(book)  # Add a book to the library

    def display_books(self):
        print("Books in Library:")
        for i, book in enumerate(self.books, start=1):
            print(f"{i}. {book}")  # Display each book with its index
        print()

    def get_book_by_number(self, number):
        if 1 <= number <= len(self.books): # Check if the number is within the range of books
            return self.books[number - 1]  # Return the book by its index
        return None


# Main function to run the program
def main():
    library = Library() # Create a library instance

    # Create book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
    book2 = Book("1984", "George Orwell", "987654321")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "567891234")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        library.display_books()  # Display all books in the library
        print("Menu:")
        print("1 - Borrow a book")
        print("2 - Return a book")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1": # Borrow a book
            book_number = input("Enter the number of the book to borrow: ")
            if book_number.isdigit(): # Check if the input is a number
                book_number = int(book_number) # Convert the input to an integer
                book = library.get_book_by_number(book_number) # Get the book by its number
                if book:
                    if book.borrow_book():
                        print(f"You borrowed '{book.title}'.")
                    else:
                        print(f"'{book.title}' is already borrowed.")
                else:
                    print("Invalid book number.")
            else:
                print("Please enter a valid number.")

        elif choice == "2": # Return a book
            book_number = input("Enter the number of the book to return: ")
            if book_number.isdigit(): # Check if the input is a number
                book_number = int(book_number) # Convert the input to an integer
                book = library.get_book_by_number(book_number) # Get the book by its number
                if book:
                    if book.return_book():
                        print(f"You returned '{book.title}'.")
                    else:
                        print(f"The book '{book.title}' has not yet been borrowed.")
                else:
                    print("Invalid book number.")
            else:
                print("Please enter a valid number.")

        elif choice == "3": # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

        print()

# Run the main function
if __name__ == "__main__":
    main()