import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values.tolist():
            print(f"'{book_name}' is already on the list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values.tolist():
            return True
        else:
            return False
    
    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
# Instantiated this class in the hw08 notebook