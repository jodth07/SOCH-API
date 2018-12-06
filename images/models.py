# images.models

from django.db import models
from rest_framework import serializers
from datetime import datetime 
# from drf_base64.fields import Base64ImageField


class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=200)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name}" 

class ImageSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)
    class Meta:
        model = Image
        exclude = ()


class Gallery(models.Model):
    name = models.CharField(max_length=200, default="my gallery")
    images = models.ManyToManyField(Image)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}" 

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        exclude = ()