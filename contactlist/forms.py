from django import forms
from .models import Contact

# Fill up form for adding contacts

# <-- RAW HTML Form Sheet -->

# class AddForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = [
#             'cname',
#             'caddress',
#             'cdescription',
#             'cnumber'
#         ]

# <-- RAW HTML Form Sheet -->

# <-- RAW DJANGO Form Sheet -->

class AddForm(forms.Form):
    cname           = forms.CharField(
            required=True, 
            label='Company Name', 
            widget=forms.TextInput(
                attrs={"placeholder":"i.e. Google"}
            )
        )
    caddress        = forms.CharField(
            required=True, 
            label='Company Address', 
            widget=forms.Textarea(
                attrs={"placeholder":"i.e. US"}
            )
        )
    cdescription    = forms.CharField(
            required=True, 
            label='Company Description', 
            widget=forms.Textarea(
                attrs={"placeholder":"i.e. Search engine"}
            )
        )
    cnumber         = forms.IntegerField(
            required=True, 
            label='Company Tel No.', 
            widget=forms.TextInput(
                attrs={"placeholder":"i.e. 9887653321"}
            )
        )
    
# <-- RAW DJANGO Form Sheet -->