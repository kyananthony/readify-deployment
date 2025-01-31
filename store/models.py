from django.db import models

class Author(models.Model):
    name= models.CharField(max_length=100)
    bio= models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class eBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pdf = models.FileField(upload_to='readify/')

def __str__(self):
    return self.title
