from django.shortcuts import redirect, render
# from django.http import HttpResponse
from .models import Contact
from .forms import AddForm

# Create your views here. ;; Request Handler

def contact_view(request):
    return render(request, 'table.html', {'contact_list':Contact.objects.all()})

# def contact_add(request):
#     form = AddForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = AddForm()
#     context = {
#     'form':form
#     }
#     return render(request, 'addForm.html', context)

def contact_add(request):
    if request.method == 'GET':
        form = AddForm()
        return render(request, 'addForm.html', {'form':form})
    else:
        form = AddForm(request.POST)
        if form.is_valid():
                form.save()
        return redirect('../contacts')

# TODO:
    # Implement post/get requests for filling the database
    # and serving json packages to be rendered in html templates.
    # Have three functions for adding, updating, and deletion.

def contact_update(request):
    return

def contact_delete(request):
    return