from django.db import models

# Create your models here.
# Make sure to run makemigrations and migrate commands to link such models

class Contact(models.Model):
    cname           = models.CharField(max_length=120)
    caddress        = models.TextField(blank=True, null=True)
    cdescription    = models.TextField(blank=True, null=True)
    cnumber         = models.PositiveSmallIntegerField()
    # cstatus         = models.BooleanField('Online')