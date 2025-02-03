from django.shortcuts import render
from .models import eBook, Author, Category
from rest_framework import viewsets, generics
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
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
def home(request):
    return render(request, 'store/home.html')

def ebook_list(request):
    ebooks = eBook.objects.all()
    return render(request, 'store/ebook_list.html', {'ebooks':ebooks})

def author_list(request):
    authors= Author.objects.all()
    return render(request, 'store/author_list.html',{'authors': authors})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})