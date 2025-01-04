from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
class Uploaded(models.Model):
    book_title=models.CharField( max_length=100)
    book_description=models.TextField()
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    year_of_published = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title