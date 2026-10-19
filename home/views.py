from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import Book

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')
        Book.objects.create(name=name, author=author)

    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get('book_name')
        author = request.POST.get('author')

        Book.objects.create(name=name, author=author)

        return redirect('home')

    return render(request, 'add_book.html')


def about(request):
    return HttpResponse("this about page")


def services(request):
    return HttpResponse("hello please provide services")