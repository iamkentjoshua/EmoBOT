from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    homeaddress = models.CharField(max_length = 100)
    province = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    birthday = models.DateField(default = datetime.now().strftime('%Y-%m-%d'))
    email = models.CharField(max_length = 100, unique=True)

    class Meta:
        db_table = "Person"

class User(Person):
    username = models.CharField(max_length = 100, unique=True)
    password = models.CharField(max_length = 100)

    class Meta:
        db_table = "User"