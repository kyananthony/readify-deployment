from django.utils import timezone
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    email = models.EmailField(default='default@example.com')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default='default-slug')

    def __str__(self):
        return self.name

class eBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pdf = models.FileField(upload_to='readify/')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
