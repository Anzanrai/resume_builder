from django.urls import path

from .views import index, education_creation_view

app_name = 'user_profile'

urlpatterns = [
    path('', index),
    path('education-create/', education_creation_view)
]