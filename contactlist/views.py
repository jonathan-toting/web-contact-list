from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ;; Request Handler

def say_hello(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request, 'index.html')

def sampleWebpage(request):
    return render(request, 'sampleWebpage.html')

def index_style(request):
    return render(request, 'css/index_style.css')

def index_behavior(request):
    return render(request, 'js/index_behavior.js')