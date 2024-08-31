# Generated by Django 5.1 on 2024-08-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('contactNumber', models.IntegerField(max_length=11)),
                ('status', models.BooleanField(verbose_name='Offline')),
            ],
        ),
    ]
