from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here. ;; Request Handler

def say_hello(request):
    return HttpResponse("Hello World")

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    obj = Contact.objects.get(id=1)
    context = {
        'object':obj
    }
    return render(request, 'base.html', context)
