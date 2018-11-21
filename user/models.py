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
from drf_writable_nested import WritableNestedModelSerializer


class Cart (models.Model):
    name = models.CharField(max_length=50, default="my cart", null=True, blank=True)
    styles = models.ManyToManyField(Style, blank=True, default="")
    products = models.ManyToManyField(Product, blank=True, default="")

    def __str__(self):
        return self.name


class CartSerializer(serializers.ModelSerializer):
    # styles = StyleSerializer(many=True, required=False)
    # products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        # fields = ('styles', 'products', 'name', 'id' )
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
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    phone = models.CharField(max_length=18, default="001 (123) 123-1234", blank=True)
    address = models.CharField(max_length=25, default="", blank=True)
    city = models.CharField(max_length=25, default="", blank=True)
    state = models.CharField(max_length=25, default="", blank=True)
    zipcode = models.CharField(blank=True, null=True, max_length=5,)
    stylist = models.BooleanField(default=False)
    
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, default="")
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, blank=True, null=True, default=[])
    
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
    cart = CartSerializer(read_only=True, required=False)
    # image = ImageSerializer(read_only=True)
 
    class Meta(object):
        model = User
        exclude = ()
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     cart_data = validated_data.pop('cart')
    #     user = User.objects.create(**validated_data)
    #     Cart.objects.create(id=user.id, **cart_data)
    #     return user

