from django.shortcuts import render
from .models import Book, Author
from django.http import HttpResponse


# Create your views here.
def books_list(request):
    books = Book.title
    return HttpResponse(books)