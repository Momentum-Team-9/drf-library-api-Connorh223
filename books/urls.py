from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_paformat_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('', views.api_root),
]
