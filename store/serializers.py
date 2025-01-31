from rest_framework import serializers
from .models import eBook, Author, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'

class eBookSerializer(serializers.ModelSerializer):
    model = eBook
    fields = '__all__'
