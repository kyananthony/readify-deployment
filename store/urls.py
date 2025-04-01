from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import eBookViewSet, AuthorViewSet, CategoryViewSet, AuthorListCreateView, home, ebook_list, author_list, category_list, category_detail, register, user_login, registration_success, get_csrf_token, logout_view

app_name = 'store'  # Add this line

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
    path('category/<slug:category_slug>/', category_detail, name='category_detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('registration-success/', registration_success, name='registration_success'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), name='password_reset_complete'),
    path('csrf/', get_csrf_token, name='csrf_token'),
    path('api/logout/', logout_view, name='logout'),
]