from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Book
from django.db.models import Q
import datetime
# Create your views here.
def home(request):
    q = request.GET.get('q','')
    if q:
        books = Book.objects.filter(
            Q(title__contains=q)|
            Q(author__contains=q)|
            Q(genre__contains=q)
        )
    else:
        books = Book.objects.all()

    context={
        'books':books
    }
    return render(request, 'home.html',context)


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        price = request.POST['price']
        publish_date = request.POST['publish_date']
        description = request.POST['description']
        
        book = Book(
            title=title,
            author=author,
            genre=genre,
            price=price,
            publish_date=publish_date,
            description=description,
        )
        book.save()

        return redirect('home')  
    return render(request, 'add_book.html')


def book_details(request,id):
    try:
        book = Book.objects.get(id=id)
    except:
        return HttpResponse('Book Not Found')
    return render(request,'book_details.html',{'book':book})

def edit_book(request,id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.genre = request.POST['genre']
        book.price = request.POST['price']
        book.publish_date =request.POST['publish_date']
        book.description = request.POST['description']
        book.save()

        return redirect('book_details', id=book.id)

    context = {
        'book': book
    }
    return render(request, 'edit_book.html', context)


def delete_book(request,id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render()

def about(request):
    return render(request,'about.html')