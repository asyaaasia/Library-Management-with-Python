class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            print("List of Books:")
            for book in books:
                title, author, release_date, pages = book.strip().split(",")
                print(f"Title: {title}, Author: {author}, Release Year: {release_date}, Pages: {pages}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_date = input("Enter the release year of the book: ")
        pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{release_date},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:
            if title in book:
                books.remove(book)
                found = True
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(books)
            print("Book removed successfully.")
        else:
            print("Book not found.")

# Creating an object named "lib" with "Library" class
lib = Library()

# Menu
while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
