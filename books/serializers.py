from rest_framework import serializers
from django.contrib.auth.models import User
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'description', 'review', 'owner',)


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')