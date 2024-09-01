from django.db import models

# Create your models here.
# Make sure to run makemigrations and migrate commands to link such models

class Contact(models.Model):
    cname           = models.CharField(max_length=120)
    caddress        = models.TextField(blank=False, null=False)
    cdescription    = models.TextField(blank=False, null=False)
    cnumber         = models.PositiveSmallIntegerField()
    cstatus         = models.BooleanField('Online')