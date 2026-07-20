from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
