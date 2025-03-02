from django.shortcuts import render, get_object_or_404
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
            login(request,user)
            return redirect('store:home')
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})