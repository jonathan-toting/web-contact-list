from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contacts
from .forms import AddForm

# Create your views here. ;; Request Handler

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    obj = Contacts.objects.get(id=1)
    context = {
        'object':obj
    }
    return render(request, 'base.html', context)

def contact_create_view(request):
    form = AddForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddForm()
    context = {
    'form':form
    }
    return render(request, 'addForm.html', context)