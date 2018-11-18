from django.db import models
from rest_framework import serializers
from images.models import Image, ImageSerializer

class Stylist(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    type = models.CharField(default="Stylist", max_length=10, editable=False)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField(blank=True, default=0, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    
    date = models.DateField(auto_now_add=True) # Added date
    udpate = models.DateField(auto_now=True)
    
    def __str__(self):
            return f"{self.name}"  

class StylistSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
  
    class Meta:
        model = Stylist
        exclude = ()
