# Generated by Django 5.1 on 2024-08-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactlist', '0002_alter_product_contactnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contactNumber',
            field=models.PositiveSmallIntegerField(),
        ),
    ]