from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name="all-categories"),
    path('categories/<int:category_id>', views.CategoryView.as_view(), name="id-categories"),


    path('products/<int:product_id>', views.ProductsView.as_view(), name='id-products'),
    path('products/', views.ProductsView.as_view(), name='all-products'),
    
    path('styles/<int:style_id>', views.StylesView.as_view(), name='id-styles'),
    path('styles/', views.StylesView.as_view(), name='all-styles'),
    
    path('cart/', views.CartView.as_view(), name="all-carts"),
    path('purchased/', views.PurchasedView.as_view(), name="all-puchases"),

    path('users/<int:user_id>', views.UsersView.as_view(), name='id-users'),
    path('users/', views.UsersView.as_view(), name='all-users'),

    path('medias/', views.ImageView.as_view(), name='id-media'),
    path('medias/<media_id>', views.ImageView.as_view(), name='id-media'),

    path('featurette/', views.FeaturetteView.as_view(), name="all-featurettes"),
    
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    
    path('group/', views.GroupView.as_view(), name="all-group")
]
