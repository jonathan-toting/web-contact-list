# Generated by Django 5.1 on 2024-09-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cweb', models.CharField(max_length=60)),
                ('cpersonel', models.CharField(max_length=60)),
                ('cemail', models.CharField(max_length=60)),
                ('cnumber', models.CharField(max_length=16)),
                ('cname', models.CharField(max_length=60)),
                ('caddress', models.TextField(blank=True, null=True)),
                ('cdescription', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
