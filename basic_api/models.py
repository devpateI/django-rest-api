from django.db import models
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    discription = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title