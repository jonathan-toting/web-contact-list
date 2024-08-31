from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. ;; Request Handler

def say_hello(request):
    return HttpResponse("Hello World")

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'base.html', {})
