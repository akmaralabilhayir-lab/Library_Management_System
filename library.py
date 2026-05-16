from file_manager import load_books, save_books

class Library:
    def __init__(self):
        self.books = load_books()

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, index):
        self.books[index]

    def borrow_book(self, index):
        if self.books[index].status == "Available":
            self.books[index].status = "Borrowed"

    def return_book(self, index):
        self.books[index].status = "Returned"

    def save_data(self):
        save_books(self.books)



