from django.db import models
from images.models import Image, ImageSerializer
from drf_writable_nested import WritableNestedModelSerializer

class Stylist(models.Model):

    type = models.CharField(default="Stylist", max_length=10, editable=False)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=25, blank=True)
    zipcode = models.IntegerField(blank=True, default=0, null=True)
    description = models.CharField(max_length=500, null=True)

    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True, default="")

    date = models.DateField(auto_now_add=True) # Added date
    udpate = models.DateField(auto_now=True)
    
    def __str__(self):
            return f"{self.name}"  

class Gallery(models.Model):
    id = models.OneToOneField(Stylist, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150, default="My Gallery")
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
            return f"{self.name}" 

class GallerySerializers(WritableNestedModelSerializer):
    image = ImageSerializer(required=False)

    class Meta:
        model = Gallery
        exclude = ()


class StylistSerializer(WritableNestedModelSerializer):
    image = ImageSerializer(required=False)
    gallery = GallerySerializers()

    class Meta:
        model = Stylist
        exclude = ()


