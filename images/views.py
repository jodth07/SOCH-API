from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Image, ImageSerializer


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
        if i_serializer.is_valid():
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
        # image.name = request.data.get("name")
        # image.image = request.data.get("image")
        
        
        serializer = ImageSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
