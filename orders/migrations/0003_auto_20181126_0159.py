# Generated by Django 2.1.1 on 2018-11-26 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181124_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50),
        ),
    ]