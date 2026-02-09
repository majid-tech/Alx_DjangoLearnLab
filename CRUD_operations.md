# CRUD Operations – Django Shell

## Create

```python
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# <Book: 1984 by George Orwell (1949)>

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

# ('1984', 'George Orwell', 1949)

book.title = "Nineteen Eighty-Four"
book.save()
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

book.delete()
Book.objects.all()

# (1, {'app.Book': 1})
# <QuerySet []>
