from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class BookData(models.Model):
    book_name = models.CharField(("Book Name"), max_length=100)
    book_author = models.CharField(("Book Author"), max_length=100)
    rating = models.IntegerField("Rating", validators = [MinValueValidator(0), MaxValueValidator(10)])
    
    def __str__(self):
        return self.book_name