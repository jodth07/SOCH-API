# users/urls.py
 
from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView, CartView, PurchasedView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create-user"),
    path('gettoken/', authenticate_user),
    path('update/', UserRetrieveUpdateAPIView.as_view(), name="update-user"),
    
    path('carts/', CartView.as_view(), name="all-carts"),
    # path('purchased/', PurchasedView.as_view(), 'all-purchased')
]
