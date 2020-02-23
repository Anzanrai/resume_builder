from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from .forms import EducationForm
from .models import Education


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

