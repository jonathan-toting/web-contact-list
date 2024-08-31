from django.db import models

# Create your models here.

class Contact(models.Model):
    companyName   = models.CharField(max_length=256)
    description   = models.TextField(blank=True, null=True)
    contactNumber = models.PositiveSmallIntegerField()
    status        = models.BooleanField('Online')