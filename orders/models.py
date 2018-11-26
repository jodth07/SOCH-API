from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from rest_framework import serializers
# Create your models here.
from carts.models import Cart
from users.models import User, Address

class UserCheckout(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True) #not required
	email = models.EmailField(unique=True) #--> required
	def __str__(self):
		self.name = f"{self.user.last_name}, {self.user.first_name}"
		return self.name
	

class UserCheckoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCheckout
        exclude = ()


ORDER_STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('shipped', 'Shipped'),
	('refunded', 'Refunded'),
)
class Order(models.Model):
	status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	user = models.ForeignKey(UserCheckout, on_delete=models.SET_NULL, null=True)
	billing_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='billing_address', null=True)
	shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='shipping_address', null=True)
	shipping_total_price = models.DecimalField(max_digits=50, decimal_places=2, default=5.99)
	order_total = models.DecimalField(max_digits=50, decimal_places=2, blank=True )
	order_id = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return f"{self.cart.id}"

	# class Meta:
	# 	ordering = ['-id']

	def mark_completed(self, order_id=None):
		self.status = "paid"
		if order_id and not self.order_id:
			self.order_id = order_id
		self.save()

	def order_pre_save(self):
		shipping_total_price = self.shipping_total_price
		cart_total = self.cart.total
		order_total = Decimal(shipping_total_price) + Decimal(cart_total)
		self.order_total = order_total


def order_pre_save(sender, instance, *args, **kwargs):
	shipping_total_price = instance.shipping_total_price
	cart_total = instance.cart.total
	order_total = Decimal(shipping_total_price) + Decimal(cart_total)
	instance.order_total = order_total

pre_save.connect(order_pre_save, sender=Order)
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        exclude = ()

