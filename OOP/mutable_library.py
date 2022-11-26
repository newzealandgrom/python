class Library:
    """Represents a library"""
    def __init__(self, books=None):
        """initialize the books"""
        if books:
            self.books = books
        else:
            self.books = []
      
    def add_book(self, book):
        """add a book to the library"""
        self.books.append(book)
        
London = Library(['Bond', 'go to'])
London.add_book('Harry Potter')
London.add_book('War and piece')
print(London.books)

new_york = Library()
new_york.add_book('The lord of the rings')
print(new_york.books)
