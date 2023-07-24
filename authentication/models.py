from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    phone = models.BigIntegerField(null=True)
    profilePicture = models.CharField(max_length=200, blank=True)
    isRenter = models.BooleanField(default=True)
    occupation = models.CharField(max_length=100, blank=True)



