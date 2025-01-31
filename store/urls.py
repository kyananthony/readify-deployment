from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import eBookViewSet, AuthorViewSet, CategoryViewSet, home, ebook_list

router = DefaultRouter()
router.register = (r'ebooks', eBookViewSet)
router.register = (r'authors', AuthorViewSet)
router.register = (r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', home, name = 'home'),
    path('ebooks/', ebook_list, name = 'ebook_list'),
]