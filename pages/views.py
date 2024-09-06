from django.shortcuts import render
# from django.http import HttpResponse
from .models import Contact
from .forms import AddForm

# Create your views here. ;; Request Handler

def contact_view(request):
    return render(request, 'table.html')

def contact_add(request):
    form = AddForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddForm()
    context = {
    'form':form
    }
    return render(request, 'addForm.html', context)

# TODO:
    # Implement post/get requests for filling the database
    # and serving json packages to be rendered in html templates.
    # Have three functions for adding, updating, and deletion.

def contact_update(request):
    return

def contact_delete(request):
    return