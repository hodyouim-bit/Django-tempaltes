import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from web.models import student

def index(request):
    context = {
        'title': "My Home Page",
        'date': datetime.date.today(),
        'students': student.objects.all(),
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
