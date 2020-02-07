from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from .models import Education


def index(request):
    return HttpResponse("I hope this works.")


class EducationListView(ListView):
    model = Education
    paginate_by = 20

