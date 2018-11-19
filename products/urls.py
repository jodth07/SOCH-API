from django.urls import path
from .views import ProductsView
 
urlpatterns = [
    path('', ProductsView.as_view(), name='all-products'),
    path('<int:product_id>', ProductsView.as_view(), name='id-products'),

]
