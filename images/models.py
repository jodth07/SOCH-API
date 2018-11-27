from django.db import models
from rest_framework import serializers
# from drf_base64.fields import Base64ImageField


class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}" 

class ImageSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)
    class Meta:
        model = Image
        exclude = ()

