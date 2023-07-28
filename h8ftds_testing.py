import unittest

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.catalog = []
    
    def display_books(self):
        if not self.catalog:
            print("The catalog is empty.")
        else:
            catalog_str = "\n".join(str(book) for book in self.catalog)
            print(f"Library catalog:\n{catalog_str}")
    
    def add_book(self, book):
        self.catalog.append(book)
        
    
    def search_by_title(self, title):
        results = [book for book in self.catalog if title.lower() in book.title.lower()]
        if results:
            print(f"Search results for '{title}':")
            for book in results:
                print(book)
        else:
            print(f"No books found with the title '{title}'.")
        return results
    
    def search_by_author(self, author):
        results = [book for book in self.catalog if author.lower() in book.author.lower()]
        if results:
            print(f"Search results for '{author}':")
            for book in results:
                print(book)
        else:
            print(f"No books found by the author '{author}'.")
        return results
    
    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.remove(book)
            print(f"Removed '{book.title}' from the catalog.")
        else:
            print(f"'{book.title}' not found in the catalog.")
    


class TestLibrary(unittest.TestCase):
    def setUp(self):

        self.library = Library()
        self.book1 = Book("Belajar Golang", "Mujahid", "9780547928227")
        self.book2 = Book("Belajar Python v2", "Mujahid", "9780747532743")
        self.book3 = Book("Belajar HTML", "Ucup", "9780451524935")

        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
    
    def test_add_book(self):
        book1 = Book("Belajar Golang", "Mujahid", "9780547928227")
        self.library.add_book(book1)
        self.assertIn(book1, self.library.catalog)
        
    def test_search_by_title(self):
        result = self.library.search_by_title("belajar python v2")
        self.assertIn(self.book2, result)

    def test_search_by_author(self):
        result = self.library.search_by_author("mujahid")
        self.assertIn(self.book2, result)
        
    def test_remove_book(self):
        self.library.remove_book(self.book2)
        self.assertNotIn(self.book2, self.library.catalog)
    
    
if __name__ == "__main__":
    unittest.main()