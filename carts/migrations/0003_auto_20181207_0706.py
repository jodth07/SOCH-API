# Generated by Django 2.1.3 on 2018-12-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='purchase_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
