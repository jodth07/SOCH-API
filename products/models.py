from django.db import models
from rest_framework import serializers

# Local imports
from images.models import Image, ImageSerializer

class Product(models.Model):
    type = models.CharField(default="Product", max_length=10, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    stored = models.IntegerField(default=20)
    requested = models.IntegerField(default=0)

    added = models.DateField(auto_now_add=True)
    purchased_date = models.DateField(blank=True, auto_now=True) # Added date

    # Relationationals 
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, default="")
   
    def __str__(self):
        return self.name


class ProductSerializer(serializers.ModelSerializer):
    
    # Serialized Relationationals 
    image = ImageSerializer()

    class Meta:
        model = Product
        exclude = ()