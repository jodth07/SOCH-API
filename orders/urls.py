from django.urls import path
from .views import OrdersView

 
urlpatterns = [
    path('', OrdersView.as_view(), name='all-orders'),
    path('<int:order_id>', OrdersView.as_view(), name='id-orders'),

]
