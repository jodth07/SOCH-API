# Generated by Django 2.1.1 on 2018-11-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='categories',
            field=models.ManyToManyField(blank=True, default='', to='api.Category'),
        ),
    ]
