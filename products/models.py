from django.db import models
from datetime import datetime  
from decimal import Decimal

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from rest_framework import serializers

from images.models import Image, ImageSerializer
from users.models import User

TAX_PERCENTAGE = 0.07

CATEGORY_CHOICES = (
    ("Style", "Style"),
    ("Product", "Product")
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)

    description = models.CharField(max_length=200)
    duration = models.IntegerField(default=0, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    company = models.CharField(max_length=100, blank=True)
    
    added = models.DateField(auto_now_add=True, blank=True, null=True)
    
    # Relationationals 
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
   
    def __str__(self):
        return self.title


class ProductSerializer(serializers.ModelSerializer):
    # image = ImageSerializer()
    
    class Meta:
        model = Product
        exclude = ()


class Variation(models.Model):
    title = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES, default="Product")
    
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.CharField(max_length=200, default="")
    
    duration = models.IntegerField(default=0, blank=True)
    
    company = models.CharField(max_length=100, blank=True, default="")
    
    added = models.DateField(auto_now_add=True, blank=True, null=True)
    purchased_date = models.DateField(blank=True, auto_now=True, null=True) # Added date

    # Relationationals 
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
   
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    inventory = models.IntegerField(null=True, blank=True)
    discount = models.DecimalField(decimal_places=2, max_digits=2, null=True, blank=True) 

    def __str__(self):
        self.title = self.product.title
        return self.title

    def get_price(self):
        self.price = self.product.price
        if self.discount is not None:
            self.sale_price = self.price - (self.price * self.discount)
            return self.sale_price
        elif self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

def product_post_saved_receiver(sender, instance, created, *args, **kwargs):
    product = instance
    variations = product.variation_set.all()
    if variations.count() == 0:
        new_var = Variation()
        new_var.product = product
        new_var.category = product.category

        new_var.title = product.title
        new_var.price = product.price
        new_var.description = product.description
        new_var.duration = product.duration
        new_var.company = product.company
        new_var.added = product.added
        new_var.image = product.image
        new_var.save()

post_save.connect(product_post_saved_receiver, sender=Product)


class VariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        exclude = ()

