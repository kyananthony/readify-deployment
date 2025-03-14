from django.shortcuts import render, redirect, get_object_or_404
from .models import eBook, Author, Category
from rest_framework import viewsets, generics
from .serializers import eBookSerializer, AuthorSerializer, CategorySerializer
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

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
    return render(request, 'store/ebook_list.html', {'ebooks': ebooks})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'store/author_list.html', {'authors': authors})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    ebooks = eBook.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {'category': category, 'ebooks': ebooks})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('store:registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store:home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('store:home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def registration_success(request):
    return render(request, 'store/registration_success.html')

def some_view(request):
    ebook_list_url = reverse('store:ebook_list')
    return redirect(ebook_list_url)