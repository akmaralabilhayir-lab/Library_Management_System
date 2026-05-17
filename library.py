from file_manager import load_books, save_books


def log_action(func):
    def wrapper(*args, **kwargs):
        print("Library action started")
        result = func(*args, **kwargs)
        print("Library action finished")
        return result

    return wrapper


class Library:
    def __init__(self):
        self.books = load_books()

    @log_action
    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.title == book.title:
                return
        self.books.append(book)

    def delete_book(self, index):
        del self.books[index]

    def borrow_book(self, index):
        if self.books[index].status == "Available":
            self.books[index].status = "Borrowed"

    def return_book(self, index):
        self.books[index].status = "Available"

    def available_books_generator(self):
        for book in self.books:
            if book.status == "Available":
                yield book

    def save_data(self):
        save_books(self.books)

    def search_book(self,keyword):
        results = []
        for book in results:
            if keyword.lower() in book.title.lower():
                results.append(book)