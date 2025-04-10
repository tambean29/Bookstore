from django.db import models

# Create your models here.
class Books(models.Model):
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField(null = True, blank= True, default= 0.0)
    
    def __str__():
        return self.bookname
