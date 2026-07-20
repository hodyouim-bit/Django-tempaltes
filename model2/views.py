import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 


def index(request):
    context = {
        'title': "My Home Page",
        'date': datetime.date.today(),
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
