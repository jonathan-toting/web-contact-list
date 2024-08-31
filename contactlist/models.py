from django.db import models

# Create your models here.
# Make sure to run makemigrations and migrate commands to link such models

class Contact(models.Model):
    companyName   = models.CharField(max_length=120)
    description   = models.TextField(blank=True, null=True)
    contactNumber = models.PositiveSmallIntegerField()
    status        = models.BooleanField('Online')