# from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
# from django.http import JsonResponse
from .models import Contact
from .forms import CreateForm

# Create your views here. ;; Request Handler

def contact_view(request):
    return render(request, 'table.html', {'contact_list' : Contact.objects.all(), 'form' : CreateForm()})


#TODO: Implement htmx
# def contact_render(request):
#     return render(request, 'tableData.html', {
#         'contact_list' : Contact.objects.all(),
#     })

# TODO:
#   Add a handler in html and js for update actions
#   Must add a convertion in the phone number section
def contact_create(request, id=0):
    print(id)
    if request.method == 'GET':
        # Identify whether the operation is insert or update
        if id == 0:
            form = CreateForm()
        else:
            entry = Contact.objects.get(pk=id)
            form = CreateForm(instance=entry)
        return render(request, 'createForm.html', {'form':form})
    else:
        if id == 0:
            form = CreateForm(request.POST)
        else:
            entry = Contact.objects.get(pk=id)
            form = CreateForm(request.POST, instance=entry)
        if form.is_valid():
                form.save()
        else:
            raise ValueError("Incorrect input!")
        return redirect('contact-view')
    
def render_selected(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CreateForm()
        else:
            entry = Contact.objects.get(pk=id)
            form = CreateForm(instance=entry)
    return render(request, 'table.html', {'contact_list' : Contact.objects.all(), 'form' : CreateForm()})
    
# def contact_add(request):
#     if request.method == 'POST':
#         form = CreateForm(request.POST)
#         if form.is_valid():
#             _temp = form.save(commit = False)
#             _temp.save()
#             return HttpResponse("Contact added successfully.")
#         else:
#             return render(request, 'CreateForm.html', {'form':form})
#     else:
#         form = CreateForm(None)
#         return render(request, 'CreateForm.html', {'form':form})

# TODO:
    # Implement post/get requests for filling the database
    # and serving json packages to be rendered in html templates.
    # Have three functions for adding, updating, and deletion.

def contact_delete(request, id):
    entry = Contact.objects.get(pk=id)
    entry.delete()
    return redirect('contact-view')