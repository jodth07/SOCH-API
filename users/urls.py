# users/urls.py
 
from django.urls import path
from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
from .views import AddressView, StylistsView
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name="create-user"),
    path('login/', authenticate_user),
    path('reup/', UserRetrieveUpdateAPIView.as_view(), name="update-user"),
    
    path('address/', AddressView.as_view(), name="all-addresses" ),
    path('address/<int:_id>', AddressView.as_view(), name="all-addresses" ),

    path('stylist/', StylistsView.as_view(), name="all-addresses" ),
    path('stylist/<int:_id>', StylistsView.as_view(), name="all-addresses" )
]
