# Generated by Django 2.1.1 on 2018-11-11 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20181110_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, default='', to='api.Product'),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='styles',
        ),
        migrations.AddField(
            model_name='cart',
            name='styles',
            field=models.ManyToManyField(blank=True, default='', to='api.Style'),
        ),
    ]
