from django.contrib import admin
from .models import User, Cart, Purchased
# Register your models here.

admin.site.register(User)
admin.site.register(Purchased)
admin.site.register(Cart)