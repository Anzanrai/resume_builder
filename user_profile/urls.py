from django.urls import path, re_path

from .views import index, education_creation_view
from . import api_views

app_name = 'user_profile'

urlpatterns = [
    # path('', index),
    # path('education-create/', education_creation_view),
    path('register/', api_views.RegistrationView.as_view(), name='register'),
    path('login/', api_views.LoginUserView.as_view(), name='login'),
    path('password_reset/', api_views.passwordreset_view, name='password_reset'),
    re_path('password_reset_done/(?P<uid>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,40})/$', api_views.passwordresetdone_view, name='password_reset_done'),
    path('password_change/', api_views.PasswordChangeView.as_view(), name='password_change'),
]