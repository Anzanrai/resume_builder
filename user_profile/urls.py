from django.urls import path

from .views import index, education_creation_view
from . import api_views

app_name = 'user_profile'

urlpatterns = [
    # path('', index),
    # path('education-create/', education_creation_view),
    path('register/', api_views.RegistrationView.as_view(), name='register'),
    path('login/', api_views.LoginUserView.as_view(), name='login'),

]