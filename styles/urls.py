from django.urls import path
from .views import StylesView

urlpatterns = [
    path('', StylesView.as_view(), name='all-styles'),
    path('<int:style_id>', StylesView.as_view(), name='id-styles'),
]