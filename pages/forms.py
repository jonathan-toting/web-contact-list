from django import forms
from .models import Contact
import phonenumbers

# Fill up form for adding Contact

class AddForm(forms.ModelForm):
    # Metadata
    class Meta:
        model = Contact
        fields = [
            'cweb',
            'cpersonel',
            'cemail',
            'cnumber',
            'cname',
            'caddress',
            'cdescription',
        ]
    # Overwrites
    cweb            = forms.CharField(
            required=True, 
            # label='Web address', 
            widget=forms.TextInput(
                # attrs={"placeholder":"i.e. www.google.com"}
            )
        )
    cpersonel       = forms.CharField(
            required=True, 
            # label='Assigned personel', 
            widget=forms.TextInput(
                # attrs={"placeholder":"i.e. Edward Stew"}
            )
        )
    cemail          = forms.EmailField(
            required=True, 
            # label='Email address', 
            widget=forms.TextInput(
                # attrs={"placeholder":"i.e. sample@sample.com"}
            )
        )
    cnumber      = forms.IntegerField(
            required=True,  
            # label='Contact #', 
            widget=forms.TextInput(
                # attrs={"placeholder":"i.e. 9887653321"}
            )
        )
    cname           = forms.CharField(
            required=True, 
            # label='Company Name', 
            widget=forms.TextInput(
                # attrs={"placeholder":"i.e. Google"}
            )
        )
    caddress        = forms.CharField(
            required=True, 
            # label='Company Address', 
            widget=forms.Textarea(
                # attrs={"placeholder":"i.e. US"}
            )
        )
    cdescription    = forms.CharField(
            required=True, 
            # label='Company Description', 
            widget=forms.Textarea(
                # attrs={"placeholder":"i.e. Search engine"}
            )
        )
    # Validations
    def clean_cweb (self, *args, **kwargs): 
        r = self.cleaned_data.get('cweb')
        return r
    
    def clean_cpersonel (self, *args, **kwargs): 
        r = self.cleaned_data.get('cpersonel')
        return r
    
    def clean_cemail (self, *args, **kwargs): 
        r = self.cleaned_data.get('cemail')
        return r
    
    def clean_cnumber(self, *args, **kwargs):
        # Ensure valid data
        parse_number = phonenumbers.parse(("+" + str(self.cleaned_data.get("cnumber"))), None)
        # Ensure valid phone number with E.164 format : [ https://en.wikipedia.org/wiki/E.164 ]
        if phonenumbers.is_possible_number(parse_number) and phonenumbers.is_valid_number(parse_number): 
            # Format as global identifier
            r = phonenumbers.format_number(parse_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            return r
        else:
            raise forms.ValidationError("Ensure phone number is valid.")
    
    def clean_cname (self, *args, **kwargs): 
        r = self.cleaned_data.get('cname')
        return r
    
    def clean_caddress (self, *args, **kwargs): 
        r = self.cleaned_data.get('caddress')
        return r
    
    def clean_cdescription (self, *args, **kwargs): 
        r = self.cleaned_data.get('cdescription')
        return r
    
    #TODO: 
        # Overwrite object names in databse
        # to be shown as such instead of object IDs.
        # Can also overwrite selection default label.