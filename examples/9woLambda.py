def book_list(books, func):
    for book in books:
        print(func(book))
books = ['System Design','Python и DevOps','Git. Практическое руководство']
def book_print(book):
    return book.upper() + ' - прочитано'
book_list(books, book_print)
