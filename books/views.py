from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from books.converters import DateConverter
from books.models import Book


def index(request):
    return redirect(reverse('books_all'))


def books_view_all(request):
    template = 'books/books_list_all.html'
    list_books_all = Book.objects.all()
    context = {'list_books': list_books_all}
    return render(request, template, context)


def books_view_date(request, pub_date: datetime):
    template = 'books/books_list_date.html'
    list_books_date = Book.objects.filter(pub_date=pub_date)
    next_date_dict = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
    if next_date_dict:
        date_next = str(next_date_dict['pub_date'])
    else:
        date_next = None
    previous_date_dict = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()
    if previous_date_dict:
        date_previous = str(previous_date_dict['pub_date'])
    else:
        date_previous = None
    context = {
        'books': list_books_date,
        'date_next': date_next,
        'date_previous': date_previous,
    }
    return render(request, template, context)
