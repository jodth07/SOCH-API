from django.db import models
from rest_framework import serializers

# Local imports
from images.models import Image, ImageSerializer

class Style(models.Model):
    type = models.CharField(default="Style", max_length=10, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    requested = models.IntegerField(default=0)
    duration = models.FloatField()
    
    added = models.DateField(auto_now_add=True) # Added date
    purchased_date = models.DateField(blank=True, auto_now=True)

    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, default="")
    
    def __str__(self):
            return self.name

class StyleSerializer(serializers.ModelSerializer):
    
    image = ImageSerializer()

    class Meta:
        model = Style
        exclude = ()

