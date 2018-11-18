from django.db import models
from rest_framework import serializers

# Local imports
from styles.models import Style, StyleSerializer
from products.models import Product, ProductSerializer
from stylists.models import Stylist, StylistSerializer


class Featurette(models.Model):
    name = models.CharField(max_length=50, default="featurette")
    updated = models.DateField(auto_now=True)

    # model relations
    style = models.OneToOneField(Style, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stylist = models.OneToOneField(Stylist, on_delete=models.CASCADE, default=1)
   

    def __str__(self):
        return self.name


class FeaturetteSerializer(serializers.ModelSerializer):

    # serializers for relations to be included
    style = StyleSerializer()
    product = ProductSerializer()
    stylist = StylistSerializer()

    class Meta:
        model = Featurette
        fields = ("stylist","style", "product" )
        # exclude = ()



# Carousel Images models