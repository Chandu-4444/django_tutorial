from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.name






    







