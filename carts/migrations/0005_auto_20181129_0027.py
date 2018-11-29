# Generated by Django 2.1.3 on 2018-11-29 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20181127_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(to='carts.CartItem'),
        ),
    ]