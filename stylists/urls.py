from django.urls import path
from .views import StylistsView
urlpatterns = [
    path('', StylistsView.as_view(), name='all-styles'),
    path('<int:stylist_id>', StylistsView.as_view(), name='id-styles'),
  
]