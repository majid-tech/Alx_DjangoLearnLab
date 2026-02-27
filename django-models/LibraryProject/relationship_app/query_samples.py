import os
import django

# Replace 'your_project_name' with your actual Django project folder name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relationship_app.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# -----------------------------------------------------
# 1️⃣ Query all books by a specific author
# -----------------------------------------------------
def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)


# -----------------------------------------------------
# 2️⃣ List all books in a library
# -----------------------------------------------------
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# -----------------------------------------------------
# 3️⃣ Retrieve the librarian for a library
# -----------------------------------------------------
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# -----------------------------------------------------
# Optional test execution
# -----------------------------------------------------
if __name__ == "__main__":
    print("Books by specific author:")
    for book in get_books_by_author("Chinua Achebe"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian for Central Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)