# Generated by Django 2.1.3 on 2018-11-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20181127_0317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='my gallery', max_length=200)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(to='images.Image'),
        ),
    ]
