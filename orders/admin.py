from django.contrib import admin

# Register your models here.

from .models import Order, UserCheckout

admin.site.register(Order)
admin.site.register(UserCheckout)