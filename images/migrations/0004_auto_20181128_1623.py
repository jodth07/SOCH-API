# Generated by Django 2.1.3 on 2018-11-28 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_stylist_gallery'),
        ('images', '0003_auto_20181128_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='images',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
