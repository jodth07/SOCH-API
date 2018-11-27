from django.urls import path
from .views import CartsView, CartItemsView

 
urlpatterns = [
    path('c/', CartsView.as_view(), name='all-carts'),
    path('c/<int:_id>', CartsView.as_view(), name='id-carts'),

    path('i/', CartItemsView.as_view(), name='all-cart-items'),
    path('i/<int:cart_item_id>', CartItemsView.as_view(), name='id-cart-items')
]
