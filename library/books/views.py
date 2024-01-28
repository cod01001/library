from django.shortcuts import render
from .models import Books

def books_index(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books_index.html', context)


def books_detail(request,pk):
    books = Books.objects.get(pk=pk)
    context = {
        'books' : books
    }
    return render(request, 'books_detail.html', context)