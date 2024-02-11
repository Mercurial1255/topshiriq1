from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name