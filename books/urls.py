from django.urls import path
from django.contrib import admin
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)