from rest_framework import serializers
from django.db import models

from users.models import User, UserSerializer
from products.models import Product, ProductSerializer

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()



class Featurette(models.Model):
    name = models.CharField(max_length=50, default="featurette")
    updated = models.DateField(auto_now=True)

    # model relations
    product = models.ManyToManyField(Product)
    stylist = models.OneToOneField(User, on_delete=models.SET_NULL, default=1, null=True)
   

    def __str__(self):
        return self.name


class FeaturetteSerializer(serializers.ModelSerializer):

    # serializers for relations to be included
    stylist = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = Featurette
        fields = ("stylist", "product" )
        # exclude = ()

