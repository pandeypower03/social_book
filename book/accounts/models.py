# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class CustomUser(AbstractUser):
    # Additional fields for custom user model
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    public_visibility = models.BooleanField(default=True)

    # Calculated field for age based on birth_year
    def calculate_age(self):
        current_year = datetime.now().year
        if self.birth_year:
            return current_year - self.birth_year
        return None

    def __str__(self):
        return self.username
