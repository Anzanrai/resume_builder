from django.urls import path

from .views import index

app_name = 'user_profile'

urlpatterns = [
    path('', index)
]