# users/models.py
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models, transaction
from rest_framework import serializers

# local imporst
from styles.models import Style, StyleSerializer
from products.models import Product, ProductSerializer
from images.models import Image, ImageSerializer


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
    styles = models.ManyToManyField(Style, blank=True, default="")
    products = models.ManyToManyField(Product, blank=True, default="")

    def __str__(self):
        return self.name

class PurchasedSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Purchased
        exclude = ()
        
 
class UserManager(BaseUserManager):
 
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25, default="")
    city = models.CharField(max_length=25, default="")
    state = models.CharField(max_length=25, default="")
    zipcode = models.IntegerField(blank=True, null=True)
    stylist = models.BooleanField(default=False)
    
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, blank=True, null=True, default="")
    purchased = models.OneToOneField(Purchased, on_delete=models.CASCADE, blank=True, null=True, default="")
    
    def __str__(self):
            return f"{self.last_name}, {self.first_name}"  

    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
 
class UserSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
    cart = CartSerializer()
    purchased = PurchasedSerializer()
    image = ImageSerializer()
 
    class Meta(object):
        model = User
        # fields = ('id', 'email', 'first_name', 'last_name',
        #           'date_joined', 'password')
        exclude = ()
        extra_kwargs = {'password': {'write_only': True}}
