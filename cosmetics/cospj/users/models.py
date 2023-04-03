from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    nickname = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    skin_type = models.CharField(max_length=30)
    address = models.CharField(max_length=50)