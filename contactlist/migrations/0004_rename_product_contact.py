# Generated by Django 5.1 on 2024-08-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactlist', '0003_alter_product_contactnumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Contact',
        ),
    ]