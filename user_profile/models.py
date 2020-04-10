from django.core.validators import URLValidator, EmailValidator
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import DateField, ValidationError


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


def validate_education_date(value):
    if value > datetime.today().date():
        raise ValidationError("This date can not be greater than present date.")
    pass


# class EducationDateField(DateField):
#     default_validators = [validate_education_date]


class Education(models.Model):
    institute = models.CharField(blank=False, null=False, max_length=300)
    level = models.CharField(blank=False, null=False, max_length=50)
    faculty = models.CharField(blank=False, null=False, max_length=300)
    start_date = models.DateField(validators=[validate_education_date])
    ongoing = models.BooleanField(default=False)
    completion_date = models.DateField(validators=[validate_education_date])
