import json
from book import Book

FILE_NAME = "book.json"

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            books = []
            for item in data:
                book = Book(
                    item["title"],
                    item["author"],
                    item["year"],
                    item["status"]
                )

                books.append(book)
            return books
    except FileNotFoundError:
        return []

def save_books(books):
    data = []
    for book in books:
        data.append(book.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
