from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import eBookViewSet, AuthorViewSet, CategoryViewSet, AuthorListCreateView, home, ebook_list, author_list, category_list

router = DefaultRouter()
router.register(r'ebooks', eBookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('ebooks/', ebook_list, name='ebook_list'),
    path('authors/list/', author_list, name='author_list'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('categories/', category_list, name='category_list'),
    path('api/', include(router.urls)),
]