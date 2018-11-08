from rest_framework import serializers
from django.db import models
from datetime import datetime
# from django.utils import timezone
import django

# Create your models here. 

class Group(models.Model):
    group = models.CharField(default="", max_length=50)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(default="example@gmail.com", max_length=50) #
    phone = models.CharField(default="5612151234", max_length=50) #
    address = models.CharField(default="here", max_length=50) #
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, default="") #
    # group = models.ForeignKey(Group, related_name='contacts', on_delete=models.CASCADE) Look up the parameters for foreign key 
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
class GroupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Group 
        exclude = ()


# Project models here. 

class Category(models.Model):
    category = models.CharField(max_length=100)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    num_requested = models.IntegerField(default=1)
    image = models.ImageField()
    created_date = models.DateField(default=django.utils.timezone.now)
    purchased_date = models.DateField(blank=True, default=django.utils.timezone.now)
    categories = models.ManyToManyField(Category)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class Style(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    num_requested = models.IntegerField(default=1)
    image = models.ImageField()
    duration = models.FloatField()
    created_date = models.DateField(default=django.utils.timezone.now)
    purchased_date = models.DateField(blank=True, default=django.utils.timezone.now)
    categories = models.ManyToManyField(Category)


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        exclude = ()


class Cart (models.Model):
    styles = models.ForeignKey(Style, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ()


class Purchased(models.Model):
    styles = models.ForeignKey(Style, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)


class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased
        exclude = ()


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField()
    email = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    stylist = models.BooleanField(default=False)
    # cart
    # purchased


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()


class Featurette(models.Model):
    style = models.OneToOneField(Style, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_date = models.DateField(default=django.utils.timezone.now)


class FeaturetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featurette
        exclude = ()

