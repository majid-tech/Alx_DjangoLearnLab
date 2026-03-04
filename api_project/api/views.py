from django.shortcuts import render
from rest_framework import generics
from .models import Book
from serializers import BookSerializer
from .views import BookList
from django.urls import path
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

urlpatterns = [
    path('books/', BookList.as_view(), name = 'book-list'), # Maps to the BookList view
]