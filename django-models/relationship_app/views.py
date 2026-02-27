from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view
def book_list(request):
    text = "<h3>Book | Author</h3>"

    books = Book.objects.all()
    for book in books:
        text += f"<p>{book.title} | {book.author.name}</p>"
    
    return HttpResponse(text)


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Correct path
    context_object_name = "library"