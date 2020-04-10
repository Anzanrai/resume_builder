from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def test_index(request):
    return HttpResponse("I hope this one works!!!")