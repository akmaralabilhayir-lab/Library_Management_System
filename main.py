import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book

library = Library()
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if not title or not author or not year:
        messagebox.showerror("Error", "Please, enter all fields")
        return

    book = Book(title, author, year)
    library.add_book(book)
    library.save_data()

    messagebox.showinfo("Success", "Book added successfully")
    clear_entries()
    show_books()

def show_books():
    listbox.delete(0, tk.END)
    for book in library.books:
        text = f"{book.title} | {book.author} | {book.year} | {book.status}"
        listbox.insert(tk.END, text)

def delete_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select book")
        return

    confirm = messagebox.askyyesno(
        "Confirm Delete", "Are you sure you want to delete this book?"
    )
    if not confirm:
        return

    index = selected[0]
    library.delete_book(index)
    library.save_data()

    show_books()

def borrow_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select book")
        return

    index = selected[0]
    library.borrow_book(index)
    library.save_data()

    show_books()

def return_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select book")
        return

    index = selected[0]
    library.return_book(index)
    library.save_data()

    show_books()

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

def search_book():
    keyword = title_entry.get()
    listbox.delete(0, tk.END)
    results = library.search_book(keyword)
    for book in results:
        text = f"{book.title} | {book.author} | {book.year} | {book.status}"
        listbox.insert(tk.END, text)

root = tk.Tk()
root.title("Library Management System")
root.geometry("600x500")
root.configure(bg="#DCEEFF")

tk.Label(root, text="Title").pack()
title_entry = tk.Entry(root, width=40)
title_entry.pack()

tk.Label(root, text="Author").pack()
author_entry = tk.Entry(root, width=40)
author_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root, width=40)
year_entry.pack()

tk.Button(root, text="Search Book",
          command=search_book,
          bg="#9C27B0",
          fg="white",).pack(pady=5)

tk.Button(root, text="Add Book",
          command=add_book,
          bg="#4CAF50",
          fg="white").pack(pady=5)

tk.Button(root, text="Delete Book",
          command=delete_book,
          bg="#F44336",
          fg="white").pack(pady=5)

tk.Button(root, text="Borrow Book",
          command=borrow_book,
          bg="#2196F3",
          fg="white").pack(pady=5)

tk.Button(root, text="Return Book",
          command=return_book,
          bg="#FF9800",
          fg="white").pack(pady=5)

listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

show_books()
root.mainloop()






