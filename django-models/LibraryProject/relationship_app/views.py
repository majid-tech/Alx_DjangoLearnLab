from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book

# Function-based view
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Correct path
    context_object_name = "library"