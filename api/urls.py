from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('products/<int:product_id>', views.ProductsView.as_view(), name='id-products'),
    path('products/', views.ProductsView.as_view(), name='all-products'),
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('group/', views.GroupView.as_view(), name="all-group")
]
