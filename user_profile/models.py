from django.core.validators import URLValidator, EmailValidator
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import DateField, ValidationError


class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    linkedin_profile = models.URLField(max_length=200, validators=[URLValidator], blank=True, null=True)
    personal_website = models.URLField(max_length=200, validators=[URLValidator], blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'address', 'phone_number']

    def __str__(self):
        return self.first_name


def validate_education_date(value):
    if value > datetime.today().date():
        raise ValidationError("This date can not be greater than present date.")
    pass


class Education(models.Model):
    institute = models.CharField(blank=False, null=False, max_length=300)
    level = models.CharField(blank=False, null=False, max_length=50)
    faculty = models.CharField(blank=False, null=False, max_length=300)
    start_date = models.DateField(validators=[validate_education_date])
    ongoing = models.BooleanField(default=False)
    completion_date = models.DateField(validators=[validate_education_date])
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.level


class Profile(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Reference(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    post = models.CharField(max_length=300, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, validators=[EmailValidator], null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def validate_start_date(value):
    if value > datetime.today().date():
        raise ValidationError("This date can not be greater than present date.")
    pass


def validate_end_date(value):
    if value < datetime.today().date():
        raise ValidationError("This date can not be smaller than start date.")


class Experience(models.Model):
    job_title = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    job_detail = models.TextField(null=True, blank=True)
    work_start_date = models.DateField(validators=[validate_start_date], null=True, blank=True)
    work_end_date = models.DateField(validators=[validate_end_date], null=True, blank=True)
    roles_and_responsibilities = models.TextField(null=True, blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title


class Certification(models.Model):
    url = models.URLField(max_length=200, validators=[URLValidator])
    provider = models.CharField(max_length=100)
    expiry_date = models.DateField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Award(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    awarded_date = models.DateField(null=True, blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Skillset(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    skills = models.TextField(null=True, blank=True)



