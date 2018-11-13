from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name="all-categories"),
    path('categories/<int:category_id>', views.CategoryView.as_view(), name="id-categories"),

    path('products/', views.ProductsView.as_view(), name='all-products'),
    path('products/<int:product_id>', views.ProductsView.as_view(), name='id-products'),

    path('styles/', views.StylesView.as_view(), name='all-styles'),
    path('styles/<int:style_id>', views.StylesView.as_view(), name='id-styles'),
    
    path('cart/', views.CartView.as_view(), name="all-carts"),
    path('cart/<int:cart_id>', views.CartView.as_view(), name="id-carts"),

    path('purchased/', views.PurchasedView.as_view(), name="all-puchases"),
    path('purchased/<int:purchased_id>', views.PurchasedView.as_view(), name="id-puchases"),

    path('users/', views.UsersView.as_view(), name='all-users'),
    path('users/<int:user_id>', views.UsersView.as_view(), name='id-users'),

    path('medias/', views.ImageView.as_view(), name='all-media'),
    path('medias/<media_id>', views.ImageView.as_view(), name='id-media'),

    path('featurette/', views.FeaturetteView.as_view(), name="all-featurettes"),
    path('featurette/<int:feat_id>', views.FeaturetteView.as_view(), name="id-featurettes"),
    
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    
    path('group/', views.GroupView.as_view(), name="all-group"),

    path('login/', obtain_jwt_token),
]
