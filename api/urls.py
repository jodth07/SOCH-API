from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('medias/', include('images.urls'))
]
