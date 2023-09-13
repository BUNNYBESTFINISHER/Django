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
    booklist=Book.objects.all()
    context = {
        'list':booklist
    }
    return render(request,'creations/index.html',context)
    
    