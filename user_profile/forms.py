from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['institute', 'level', 'faculty', 'start_date', 'ongoing', 'completion_date']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_completion_date = cleaned_data.get('completion_date', None)
        cleaned_start_date = cleaned_data.get('start_date', None)
        cleaned_ongoing = cleaned_data.get('ongoing')

        if not cleaned_start_date:
            raise ValidationError("Education start date not provided.")

        if not cleaned_ongoing:
            if not cleaned_completion_date:
                raise ValidationError("Education completion date not provided.")

            elif cleaned_completion_date:
                if cleaned_completion_date < cleaned_start_date:
                    raise ValidationError("Education completion date can not be older than start date.")

