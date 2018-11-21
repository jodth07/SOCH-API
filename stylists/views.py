from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Stylist, StylistSerializer

# Create your views here.
        
    
class StylistsView(APIView):
    """
    get:
    Return a list of all existing styles 
    
    post:
    Create a new style 
    
    put:
    Update a style
    
    delete:
    Delete a style
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses = {status.HTTP_200_OK : StylistSerializer(many=True)}
    )
    def get(self, request, style_id=None):
        if style_id is not None:
            style = Stylist.objects.get(id=style_id)
            serializer = StylistSerializer(style, many=False)
            return Response(serializer.data)
        else:
            styles = Stylist.objects.all()
            serializer = StylistSerializer(styles, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body = StylistSerializer,
        responses = {
            status.HTTP_200_OK : StylistSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
        }
    )
    def post(self, request):
        s_serializer = StylistSerializer(data=request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(s_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response = {status.HTTP_204_NO_CONTENT}
    )
    def delete(self, request, style_id):
        style = Stylist.objects.get(id=style_id)
        style.delete()
        return Response(status.HTTP_204_NO_CONTENT)


    @swagger_auto_schema(
        responses = {
            status.HTTP_200_OK : StylistSerializer,
            status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )
    def put(self, request, style_id):
        style = Stylist.objects.get(id=style_id)
    

        serializer = StylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
      
