from django.urls import path
from .views import ProductsView, VariationsView, StyleListView

 
urlpatterns = [
    path('p/', ProductsView.as_view(), name='all-products'),
    path('s/', StyleListView.as_view(), name='all-styles'),
    path('p/<int:product_id>', ProductsView.as_view(), name='id-products'),

    path('v/', ProductsView.as_view(), name='all-variations'),
    path('v/<int:variation_id>', ProductsView.as_view(), name='id-variations')
]
