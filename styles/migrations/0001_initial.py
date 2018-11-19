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
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='Style', editable=False, max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('requested', models.IntegerField(default=0)),
                ('duration', models.FloatField()),
                ('added', models.DateField(auto_now_add=True)),
                ('purchased_date', models.DateField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image')),
            ],
        ),
    ]
