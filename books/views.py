from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'books': reverse('book-list', request=request, format=format) 
    })