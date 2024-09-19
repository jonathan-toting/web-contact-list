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
            Q(cweb__icontains = searched) | 
            Q(cpersonel__icontains = searched) | 
            Q(cemail__icontains = searched) | 
            Q(cnumber__icontains = searched) | 
            Q(cname__icontains = searched) | 
            Q(caddress__icontains = searched) | 
            Q(cdescription__icontains = searched)
        )
        contact_list = Contact.objects.filter(multiple_searched)
        return render(request, 'dataSearch.html', {'searched' : searched, 'contact_list' : contact_list})
    else:
        return render(request, 'dataSearch.html', {})
    
def contact_delete(request, id):
    entry = Contact.objects.get(pk=id)
    entry.delete()
    return redirect('contact-view')