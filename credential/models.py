from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    Mobile = models.CharField(max_length=18)
    newsLetter=models.BooleanField(default=True)
    email=models.CharField(max_length=255, null=True)

class sendFriends(models.Model):
    email = models.CharField(max_length=255, null=True,unique=True)
    sharedlink=models.CharField(max_length=2000, null=True)
