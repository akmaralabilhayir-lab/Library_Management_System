import tkinter as tk
from tkinter import messagebox
from library import Library
from book import Book

library = Library()
def add_book():
    try:
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        year = year_entry.get().strip()

        if not title or not author or not year:
            messagebox.showerror("Error", "Please, enter all fields")
            return

        if not year.isdigit() or len(year) != 4:
            messagebox.showerror("Error", "Year must be 4digit number")
            return

        if len(title) > 150:
            messagebox.showerror("Error", "Title too long (max 150 characters)")
            return

        if len(author) > 100:
            messagebox.showerror("Error", "Author name too long (max 100 characters)")
            return

        book = Book(title, author, year)
        if library.add_book(book):
            library.save_data()
            messagebox.showinfo("Success", "Book added successfully")
            clear_entries()
            show_books()
        else:
            messagebox.showerror("Error", "Book with this title already exists")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book: {str(e)}")

def show_books():
    listbox.delete(0, tk.END)
    for book in library.books:
        text = f"{book.title} | {book.author} | {book.year} | {book.status}"
        listbox.insert(tk.END, text)
    count_label.config(text=f"Total books: {len(library.books)}")

def delete_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select book")
        return

    confirm = messagebox.askyesno(
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
root.geometry("900x650")
root.configure(bg="#F4F7FF")

title_label = tk.Label(root, text="Library Management System",
    font=("Helvetica", 24, "bold"),
    bg="#F4F7FF", fg="#1A237E"
)
title_label.pack(pady=20)

input_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
input_frame.pack(pady=10, padx=20, fill="x")
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=3)

tk.Label(input_frame, text="Title", font=("Arial", 11, "bold"),
         bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
title_entry = tk.Entry(input_frame, width=40, font=("Arial", 12), bd=3)
title_entry.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Author", font=("Arial", 11, "bold"),
         bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
author_entry = tk.Entry(input_frame, width=40, font=("Arial", 12), bd=3)
author_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Year", font=("Arial", 11, "bold"),
         bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
year_entry = tk.Entry(input_frame, width=40, font=("Arial", 12), bd=3)
year_entry.grid(row=2, column=1)

count_label = tk.Label(root,text="Total books: 0",
    font=("Arial", 12, "bold"), bg="#F4F7FF", fg="#333"
)
count_label.pack()


button_frame = tk.Frame(root, bg="#F4F7FF")
button_frame.pack(pady=20)
btn_style = {"font": ("Arial", 10, "bold"),
    "width": 14, "height": 2,
    "bd": 0, "cursor": "hand2"
}

tk.Button(button_frame, text="Search Book", command=search_book,
           bg="#9C27B0",fg="white", **btn_style).grid(row=0, column=0, padx=8)

tk.Button(button_frame, text="Add Book", command=add_book,
          bg="#4CAF50", fg="white", **btn_style).grid(row=0, column=1, padx=8)

tk.Button(button_frame, text="Delete Book", command=delete_book,
          bg="#F44336", fg="white", **btn_style).grid(row=0, column=2, padx=8)

tk.Button(button_frame, text="Borrow Book", command=borrow_book,
          bg="#2196F3", fg="white", **btn_style).grid(row=0, column=3, padx=8)

tk.Button(button_frame, text="Return Book", command=return_book,
          bg="#FF9800", fg="white", **btn_style).grid(row=0, column=4, padx=8)


list_frame = tk.Frame(root)
list_frame.pack(pady=15)

scrollbar = tk.Scrollbar(list_frame)
listbox = tk.Listbox(list_frame,width=90, height=15,
    font=("Consolas", 11), bd=2, relief="solid",
    yscrollcommand=scrollbar.set,
    selectbackground="#4CAF50",
    selectforeground="white"
)

scrollbar.config(command=listbox.yview)
listbox.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

show_books()
root.mainloop()






