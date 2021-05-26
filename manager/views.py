from django.shortcuts import redirect, render
from .models import Author, Book
from django.db.models import Q


def red_app_home(request):
    return redirect('/')


def app_home(request):
    return render(request, 'home.html', {"books": Book.objects.all(), "authors": Author.objects.all(), "last": ""})


def home_search(request):
    if request.POST.get("search"):
        s = request.POST.get("search")
        authors = Author.objects.filter((Q(first_name__contains=s) | Q(last_name__contains=s)))
        books = Book.objects.filter((Q(title__contains=s) | Q(isbn__contains=s)))
    return render(request, 'home.html', {"books": books, "authors": authors, "last": ""})


def home_remove(request):
    if request.GET.get("id") and request.GET.get("cat"):
        if request.GET.get("cat") == 'author':
            if Author.objects.get(id=request.GET.get("id")):
                Author.objects.get(id=request.GET.get("id")).delete()
        else:
            if Book.objects.get(id=request.GET.get("id")):
                Book.objects.get(id=request.GET.get("id")).delete()

    return redirect('/')


def author_home(request):
    return render(request, 'author/index.html', {"authors": Author.objects.all(), "last": ""})


def book_home(request):
    return render(request, 'book/index.html',
                  {"books": Book.objects.all(), "authors": Author.objects.all(), "last": ""})


def remove_author(request):
    if request.GET.get("id") and Author.objects.get(id=request.GET.get("id")):
        Author.objects.get(id=request.GET.get("id")).delete()

    return render(request, 'author/index.html', {"authors": Author.objects.all(), "last": ""})


def remove_book(request):
    if request.GET.get("id") and Book.objects.get(id=request.GET.get("id")):
        Book.objects.get(id=request.GET.get("id")).delete()

    return render(request, 'book/index.html',
                  {"books": Book.objects.all(), "authors": Author.objects.all(), "last": ""})


def save_author(request):
    author = None
    if request.method == 'POST':
        if request.POST.get("id") and Author.objects.get(id=request.POST.get("id")):
            author = Author.objects.get(id=request.POST.get("id"))

            if request.POST.get("first_name") and request.POST.get("last_name"):
                author.first_name = request.POST.get("first_name")
                author.last_name = request.POST.get("last_name")
                author.save()

        elif request.POST.get("first_name") and request.POST.get("last_name"):
            author = Author(first_name=request.POST.get("first_name", ""), last_name=request.POST.get("last_name"))
            author.save()

    return render(request, 'author/index.html', {"authors": Author.objects.all(), "last": author if author else ""})


def save_book(request):
    book = None
    if request.method == 'POST':
        if request.POST.get("id") and Book.objects.get(id=request.POST.get("id")):
            book = Book.objects.get(id=request.POST.get("id"))

            if request.POST.get("title") and request.POST.get("isbn") and request.POST.get("author_id"):
                book.title = request.POST.get("title")
                book.isbn = request.POST.get("isbn")
                author = Author.objects.get(id=request.POST.get("author_id"))
                book.author = author
                book.save()

        elif request.POST.get("title") and request.POST.get("isbn") and request.POST.get("author_id"):
            book = Book(title=request.POST.get("title", ""), isbn=request.POST.get("isbn"))
            book.author = Author.objects.get(id=request.POST.get("author_id"))
            book.save()

    return render(request, 'book/index.html',
                  {"books": Book.objects.all(), "authors": Author.objects.all(), "last": book if book else ""})

