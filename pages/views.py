from django.shortcuts import redirect, render
from .models import Contact
from .forms import CreateForm

def contact_view(request):
    return render(request, 'dataView.html', {'contact_list' : Contact.objects.all()})

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
    
def contact_search(request):
    return render(request, 'dataSearch.html', {})
    
def contact_delete(request, id):
    entry = Contact.objects.get(pk=id)
    entry.delete()
    return redirect('contact-view')