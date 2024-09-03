from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import AddForm

# Create your views here. ;; Request Handler

# Raw HTML form method
# form = AddForm(request.POST or None)
# if form.is_valid():
#    form.save()
#    form = AddForm()
# context = {
#   'form':form
# }

# def contact_create_view(request):
#     form = AddForm()
#     if request.method == 'POST':
#         form = AddForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # Pass in verified data with ** to convert to args
#             Contact.objects.create(**form.cleaned_data)
#         else :
#             print(form.errors)
#     context = {
#         'form':form
#     }
#     return render(request, 'addForm.html', context)

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    obj = Contact.objects.get(id=10)
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

# def homepage_view(request, *args, **kwargs):
#     print(args, kwargs)
#     print(request.user)
#     return render(request, 'homepage.html')
