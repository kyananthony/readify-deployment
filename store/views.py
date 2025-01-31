from django.shortcuts import render
from .models import eBook
from rest_framework import viewsets
from .models import eBook, Author, Category
from .serializers import eBookSerializer, AuthorSerializer, CategorySerializer
from django.http import HttpResponse

class eBookViewSet(viewsets.ModelViewSet):
    queryset = eBook.objects.all()
    serializer_class = eBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def home(request):
    return render(request, 'store/home.html')

def ebook_list(request):
    ebooks = eBook.objects.all()
    return render(request, 'store/ebook_list.html', {'ebooks':ebooks})
