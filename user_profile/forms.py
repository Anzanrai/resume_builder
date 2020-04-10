from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Education


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


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
