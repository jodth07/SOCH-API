# Generated by Django 2.1.3 on 2018-11-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181128_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.IntegerField(default=0),
        ),
    ]
