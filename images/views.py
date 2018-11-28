# images.views

from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Image, ImageSerializer
from .models import Gallery, GallerySerializer

class ImageView(APIView):
    """
    get:
    Return a list of all existing images/medias 
    
    post:
    Add new Image
    
    put:
    Update a contact
    
    delete:
    Delete an image
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ImageSerializer(many=True)}
    )
    def get(self, request, media_id=None):
        if media_id is not None:
            try:
                int(media_id)
                image = Image.objects.get(id=media_id)
                image_data = open(image.image.path, "rb").read()
                return HttpResponse(image_data, content_type="image/png")
            except:
                image = Image.objects.get(image=media_id)
                image_data = open(image.image.path, "rb").read()
                return HttpResponse(image_data, content_type="image/png")

        else:
            images = Image.objects.all()
            serializer = ImageSerializer(images, context={"request": request}, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ImageSerializer,
        responses={
            status.HTTP_200_OK : ImageSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request, *args, **kwargs):
        i_serializer = ImageSerializer(data=request.data)
        if i_serializer.is_valid(raise_exception=True):
            i_serializer.save()
            return Response(i_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(i_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, media_id):
    
        image = Image.objects.get(id=media_id)
        image.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : ImageSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, media_id):
        
        image = Image.objects.get(id=media_id)
        
        serializer = ImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GallerysView(APIView):
    """
    get:
    Return a list of all existing gallerys

    get: <id> 
    Return gallery with embeddeded image object

    post:
    Create a new gallery, along with create embeded image object 
    
    put:
    Update a gallery
    
    delete:
    Delete the specified gallery along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : GallerySerializer(many=True)}
    )
    def get(self, request, media_id=None):

        if media_id is not None:
            # gallery = Gallery.objects.filter(id=media_id, purchased=False)
            gallery = Gallery.objects.get(id=media_id)
            serializer = GallerySerializer(gallery, many=False)
            return Response(serializer.data)
        else:
            gallerys = Gallery.objects.all()
            serializer = GallerySerializer(gallerys, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=GallerySerializer,
        responses={
            status.HTTP_200_OK : GallerySerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, media_id):
        
        gallery = Gallery.objects.get(id=media_id)
        gallery.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : GallerySerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, media_id):
        
        gallery = Gallery.objects.get(id=media_id)
        
        serializer = GallerySerializer(gallery, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 