from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    review = models.TextField(max_length=750)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
