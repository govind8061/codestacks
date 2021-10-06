from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_activity(request):
    return HttpResponse("<h1>Hi Guys</h1>")