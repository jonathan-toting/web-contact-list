from django.db import models

# Create your models here.
# Make sure to run makemigrations and migrate commands to link such models

class Contact(models.Model):
    # TODO: Insert company web link
    cweb            = models.CharField(max_length=60)
    # ... Company personel info ...
    cpersonel       = models.CharField(max_length=60)
    cemail          = models.CharField(max_length=60) 
    cnumber         = models.CharField(max_length=16)
    # ... Company info ...
    cname           = models.CharField(max_length=60)
    caddress        = models.TextField(blank=True, null=True)
    cdescription    = models.TextField(blank=True, null=True)
    # cstatus         = models.BooleanField('Online')