from django.urls import path, include
from .views import FeaturetteView

urlpatterns = [
    path('users/', include('user.urls')),
    path('medias/', include('images.urls')),
    path('products/', include('products.urls')),
    path('styles/', include('styles.urls')),
    path('stylists/', include('stylists.urls')),

# Home
    path('featurette/', FeaturetteView.as_view(), name="all-featurettes"),
    path('featurette/<int:feat_id>', FeaturetteView.as_view(), name="id-featurettes")
]
