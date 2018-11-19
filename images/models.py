from django.db import models
from rest_framework import serializers


class Image(models.Model):
    image = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}" 

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        exclude = ()

