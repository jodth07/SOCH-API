# Generated by Django 2.1.3 on 2018-11-28 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_stylist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylist',
            name='gallery',
        ),
    ]
