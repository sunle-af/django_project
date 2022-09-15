from importlib.resources import contents
from operator import mod
from turtle import title
from typing_extensions import Self
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) ##only when it is created auto_now -->only when updated
    author = models.ForeignKey(User, on_delete=models.CASCADE) ##delte everything

    def __str__(self):
        return self.title
