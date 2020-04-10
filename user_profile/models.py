from django.core.validators import URLValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50,unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    linkedin_profile = models.URLField(max_length=200, validators=[URLValidator])
    personal_website = models.URLField(max_length=200, validators=[URLValidator])

    REQUIRED_FIELDS = ['email']