# Generated by Django 2.1.1 on 2018-11-19 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stylists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylist',
            name='image',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Image'),
        ),
    ]
