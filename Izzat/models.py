from django.contrib.auth.models import AbstractUser
from django.db import models

class Author(AbstractUser):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class Post(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField()

