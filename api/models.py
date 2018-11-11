from rest_framework import serializers
from django.db import models
from datetime import datetime
# from django.utils import timezone
import django
from django.core.files import File
import base64

# Create your models here. 

class Group(models.Model):
    group = models.CharField(default="", max_length=50)
    
    def __str__(self):
        return self.group

class GroupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Group 
        exclude = ()
   


class Contact(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(default="example@gmail.com", max_length=50) #
    phone = models.CharField(default="5612151234", max_length=50) #
    address = models.CharField(default="here", max_length=50) #
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, default="") #
    # group = models.ForeignKey(Group, related_name='contacts', on_delete=models.CASCADE) Look up the parameters for foreign key 

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
   

# Project models here. 
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


class Category(models.Model):
    ITEM_TYPES = (
        ('S', 'Style'),
        ('P', 'Product'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=ITEM_TYPES, default='P')
    
    def __str__(self):
        return self.name

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
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    created_date = models.DateField(auto_now_add=True)
    purchased_date = models.DateField(blank=True, auto_now=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        exclude = ()

class Style(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    num_requested = models.IntegerField(default=1)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    duration = models.FloatField()
    created_date = models.DateField(default=django.utils.timezone.now)
    purchased_date = models.DateField(blank=True, default=django.utils.timezone.now)
    categories = models.ManyToManyField(Category, blank=True, default="")

    def __str__(self):
            return self.name

class StyleSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Style
        exclude = ()


class Cart (models.Model):
    name = models.CharField(max_length=50, default="my cart")
    styles = models.ManyToManyField(Style, blank=True, default="")
    products = models.ManyToManyField(Product, blank=True, default="")

    def __str__(self):
        return self.name

class CartSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        # fields = ('styles', 'products', 'name', 'id' )
        exclude = ()


class Purchased(models.Model):
    name = models.CharField(max_length=50, default="my purchase history")
    styles = models.ForeignKey(Style, on_delete=models.CASCADE, blank=True, default="")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default="")

    def __str__(self):
        return self.name

class PurchasedSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Purchased
        exclude = ()



class User(models.Model):
    image = models.ImageField(null=True, default="", blank=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField()
    stylist = models.BooleanField(default=False)
    
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, blank=True, null=True, default="")
    purchased = models.OneToOneField(Purchased, on_delete=models.CASCADE, blank=True, null=True, default="")
    
    def __str__(self):
            return f"{self.last_name}, {self.first_name}"  

class UserSerializer(serializers.ModelSerializer):
    purchased = PurchasedSerializer()
    cart = CartSerializer()

    class Meta:
        model = User
        exclude = ()



class Featurette(models.Model):
    name = models.CharField(max_length=50, default="featurette")
    style = models.OneToOneField(Style, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name

class FeaturetteSerializer(serializers.ModelSerializer):
    style = StyleSerializer()
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = Featurette
        exclude = ()

