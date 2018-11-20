from django.db import models
from drf_writable_nested import WritableNestedModelSerializer

# Local imports
from images.models import Image, ImageSerializer


class Style(models.Model):
    type = models.CharField(default="Style", max_length=10, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    requested = models.IntegerField(default=0)
    
    duration = models.IntegerField(default=15)

    added = models.DateField(auto_now_add=True)
    purchased_date = models.DateField(blank=True, auto_now=True) # Added date

    # Relationationals 
    image = models.OneToOneField(Image, on_delete=models.CASCADE, default="")
   
    def __str__(self):
        return self.name


class StyleSerializer(WritableNestedModelSerializer):
    
    # Serialized Relationationals 
    image = ImageSerializer()

    class Meta:
        model = Style
        exclude = ()

