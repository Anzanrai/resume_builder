from datetime import datetime

from django.db import models

# Create your models here.
from django.forms import DateField, ValidationError


def validate_education_date(value):
    if value > datetime.today():
        raise ValidationError("This date can not be greater than present date.")
    pass


class EducationDateField(DateField):
    default_validators = [validate_education_date]


class Education(models):
    institute = models.CharField(blank=False, null=False)
    level = models.CharField(blank=False, null=False)
    faculty = models.CharField(blank=False, null=False)
    start_date = EducationDateField(blank=False, null=False)
    ongoing = models.BooleanField(default=False)
    completion_date = EducationDateField(blank=True)

