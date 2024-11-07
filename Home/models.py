from django.contrib.auth.models import User 
from django.db import models 
from django.utils import timezone
from django.core.exceptions import ValidationError


class Register(models.Model):
        name = models.CharField(max_length=25)
        phone = models.CharField(max_length=10)
        email = models.EmailField()
        username=models.CharField(max_length=50)
        password=models.CharField(max_length=50)
       


