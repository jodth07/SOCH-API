from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Style, StyleSerializer
from images.models import Image

import traceback

# Create your views here.
    
class StylesView(APIView):
    """
    get:
    Return a list of all existing styles 

    get: <id>
    Return an existing style with its embedded image object
    
    post:
    Create a new style with its embedded image object
    
    put:
    Update a style along with its embedded image object
    
    delete:
    Delete a style along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses = {status.HTTP_200_OK : StyleSerializer(many=True)}
    )
    def get(self, request, style_id=None):
        if style_id is not None:
            style = Style.objects.get(id=style_id)
            serializer = StyleSerializer(style, many=False)
            return Response(serializer.data)
        else:
            styles = Style.objects.all()
            serializer = StyleSerializer(styles, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body = StyleSerializer,
        responses = {
            status.HTTP_200_OK : StyleSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
        }
    )
    def post(self, request):
        serializer = StyleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response = {status.HTTP_204_NO_CONTENT}
    )
    def delete(self, request, style_id):
        style = Style.objects.get(id=style_id)
        image = Image.objects.get(id=style.image.id)
        image.delete()
        return Response(status.HTTP_204_NO_CONTENT)


    @swagger_auto_schema(
        responses = {
            status.HTTP_200_OK : StyleSerializer,
            status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )
    def put(self, request, style_id):
        style = Style.objects.get(id=style_id)
        
        serializer = StyleSerializer(style, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
      
