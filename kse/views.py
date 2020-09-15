from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, "kse/index.html")

def about(request):
    return render(request, 'kse/about.html')

def contact(request):
    return render(request, 'kse/contact.html')

def services(request):
    return render(request, 'kse/services.html')