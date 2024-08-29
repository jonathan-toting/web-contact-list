from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ;; Request Handler

def calc(f):
    r = f * 7
    u = r * 9
    return u * 10

def say_hello(request):
    x = 1
    y = 2
    z = x + 2
    p = calc(5)
    return HttpResponse("Hello World")

def index(request):
    x = 1
    y = 2
    z = x + 2
    p = calc(5)
    return render(request, 'hello.html', {'name':'Pie'})