# Generated by Django 2.1.1 on 2018-11-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Stylist', editable=False, max_length=10)),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(default='001 (123) 123-1234', max_length=18)),
                ('address', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zipcode', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('udpate', models.DateField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image')),
            ],
        ),
    ]
