class Book:
    def __init__(self, title, author, year, status="Available"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    def to_dict(self):
        return {
            "title":  self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

