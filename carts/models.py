from django.db import models
from datetime import datetime  
from decimal import Decimal
from django.db.models.signals import post_save

# Create your models here.
from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from rest_framework import serializers

from users.models import User
from products.models import Product, Variation, VariationSerializer, ProductSerializer

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey(Variation, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0.00)

    def __str__(self):
        return self.product.title

    def set_total(self):
        self.subtotal = self.product.sale_price * self.quantity
        return self.subtotal

    def remove(self):
        if self.quantity < 1:
            return self.delete()

def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
	qty = instance.quantity
	if qty >= 1:
		price = instance.product.get_price()
		subtotal = Decimal(qty) * Decimal(price)
		instance.subtotal = subtotal

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)

def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
	instance.cart.update_subtotal()

post_save.connect(cart_item_post_save_receiver, sender=CartItem)

post_delete.connect(cart_item_post_save_receiver, sender=CartItem)

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = CartItem
        exclude = ()

class CartItemCreateUpdateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CartItem
        exclude = ()


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Variation, through=CartItem)

    purchased = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, default=None )
    
    updated = models.DateField(auto_now=True)
      
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax_percentage  = models.DecimalField(max_digits=10, decimal_places=5, default=0.065)
    tax_total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)

    # payment_token = models.CharField(max_length=500, null=True, default=None)
    # payment_id = models.CharField(max_length=500, null=True, default=None)

    def set_purchase_date(self):
        if self.purchased:
            self.purchase_date = datetime.now

    def __str__(self):
        return self.user.first_name + "_" + str(self.id)

    def update_subtotal(self):
        subtotal = 0
        products = self.cartitem_set.all()
        for product in products:
            subtotal += product.subtotal
        self.subtotal = "%.2f" %(subtotal)
        self.save()


def do_tax_and_total_receiver(sender, instance, *args, **kwargs):
	subtotal = Decimal(instance.subtotal)
	tax_total = round(subtotal * Decimal(instance.tax_percentage), 2)
	total = round(subtotal + Decimal(tax_total), 2)
	instance.tax_total = "%.2f" %(tax_total)
	instance.total = "%.2f" %(total)
	#instance.save()

pre_save.connect(do_tax_and_total_receiver, sender=Cart)


def user_post_saved_receiver(sender, instance, created, *args, **kwargs):
    user = instance
    carts = user.cart_set.all()
    if carts.count() == 0:
        new_var = Cart()
        new_var.user = user
        new_var.save()

post_save.connect(user_post_saved_receiver, sender=User)



# def cart_post_save_receiver(sender, instance, *args, **kwargs):
# 	instance.cart.update_subtotal()

# post_save.connect(cart_post_save_receiver, sender=Cart)


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        exclude = ()

