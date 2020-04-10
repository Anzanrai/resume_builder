from django.urls import path

from .views import test_index

app_name = 'testapp'

urlpatterns = [
    path('', test_index)
]