from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ;; Request Handler

def say_hello(request):
    return HttpResponse("Hello World")

def index(request):
    return render(request, 'hello.html')