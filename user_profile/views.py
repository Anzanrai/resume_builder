from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import User
from django.views.generic import CreateView, ListView

from .forms import EducationForm
from .models import Education


def RegisterView(request):
    form = RegisterForm(request.POST)
    if request.method == 'POSt':
        if form.is_valid():
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User(first_name=firstname, last_name=lastname, username=username, address=address,
                        email=email)
            user.set_password(password)
            user.save()


def LoginView(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)


def index(request):
    return HttpResponse("I hope this works.")


def education_creation_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Education data has been successfully added.")
    else:
        form = EducationForm()
    return render(request, 'education_template.html', {'form': form})


class EducationListView(ListView):
    model = Education
    paginate_by = 20
