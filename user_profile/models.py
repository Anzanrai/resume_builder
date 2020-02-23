from datetime import datetime

from django.db import models

# Create your models here.
from django.forms import DateField, ValidationError


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

