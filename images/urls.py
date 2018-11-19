# images/urls.py

 
from django.urls import path
from .views import ImageView
 
urlpatterns = [
    path('', ImageView.as_view(), name='all-media'),
    path('<media_id>', ImageView.as_view(), name='id-media')
]
