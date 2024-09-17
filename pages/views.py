from django.shortcuts import redirect, render
from .models import Contact
from .forms import CreateForm
from django.db.models import Q

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
    if request.method == "POST":
        searched = request.POST['searched']
        multiple_searched = Q(
            Q(cweb__contains = searched) | 
            Q(cpersonel__contains = searched) | 
            Q(cemail__contains = searched) | 
            Q(cnumber__contains = searched) | 
            Q(cname__contains = searched) | 
            Q(caddress__contains = searched) | 
            Q(cdescription__contains = searched)
        )
        contact_list = Contact.objects.filter(multiple_searched)
        return render (request, 'dataSearch.html', {'searched' : searched, 'contact_list' : contact_list})
    else:
        return render(request, 'dataSearch.html', {})
    
def contact_delete(request, id):
    entry = Contact.objects.get(pk=id)
    entry.delete()
    return redirect('contact-view')