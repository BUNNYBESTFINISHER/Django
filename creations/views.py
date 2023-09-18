from django.shortcuts import render
from django.http import HttpResponse
from flask import redirect
from .models import Book
from .forms import BookForm
import logging
logger = logging.getLogger(__name__)
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
def update(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
        form = BookForm(request.POST or None,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse('http://127.0.0.1:8000/')

        else:
            print("not possible")
    except Exception as e:
        print(f"error was{str(e)}")
        logger.error(f"Error:{str(e)}")
    return render(request,'creations/edit.html',{'form':form,'book':book})
def delete(request,id):
    if request.method =="POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'creations/delete.html')