import json
from book import Book

FILE_NAME = "data/book.json"

def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()

            if not content:
                return []
            data = json.loads(content)

            if not data:
                return []

            books = []
            for item in data:
                try:
                    book = Book(
                        item["title"], item["author"],
                        item["year"], item.get("status", "Available")
                    )
                    books.append(book)
                except KeyError as e:
                    print(f"Warning: Skipping invalid book - missing {e}")
                    continue
            return books

    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Warning: JSON corrupted ({e}). Starting fresh.")
        return []
    except Exception as e:
        print(f"Error loading books: {e}")
        return []

def save_books(books):
    data = []
    for book in books:
        data.append(book.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)