from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello, World! I'm Model2 web app.")
