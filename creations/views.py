from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
def index(request):
    booklist=Book.objects.all()
    context = {
        'list':booklist
    }
    return render(request,'creations/index.html',context)
def details(request,book_id):
    booklist=Book.objects.get(id=book_id)
    return render(request,'creations/detail.html',{'book':booklist})

def add_book(request):
    if request.method =='POST':
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = Book(name = name,desc = desc, price = price, book_image = book_image)
        book.save()

    return render(request,'creations/add_book.html')
    
    