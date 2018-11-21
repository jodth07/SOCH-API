# users/urls.py
 
from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView, CartView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create-user"),
    path('login/', authenticate_user),
    path('reup/', UserRetrieveUpdateAPIView.as_view(), name="update-user"),
    
    path('carts/', CartView.as_view(), name="all-carts"),
    path('carts/<int:cart_id>', CartView.as_view(), name="all-carts")
]
