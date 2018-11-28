# images/urls.py

 
from django.urls import path
from .views import ImageView, GallerysView
 
urlpatterns = [
    path('', ImageView.as_view(), name='all-media'),
    path('<media_id>', ImageView.as_view(), name='id-media'),
    path('g/', GallerysView.as_view(), name='all-media'),
    path('g/<media_id>', GallerysView.as_view(), name='all-media')
]
