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
    Return a list of all existing stylists 
    
    post:
    Create a new stylist 
    
    put:
    Update a stylist
    
    delete:
    Delete a stylist
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses = {status.HTTP_200_OK : StylistSerializer(many=True)}
    )
    def get(self, request, stylist_id=None):
        if stylist_id is not None:
            stylist = Stylist.objects.get(id=stylist_id)
            serializer = StylistSerializer(stylist, many=False)
            return Response(serializer.data)
        else:
            stylists = Stylist.objects.all()
            serializer = StylistSerializer(stylists, many=True)
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
        if s_serializer.is_valid(raise_exception=True):
            s_serializer.save()
            return Response(s_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(s_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response = {status.HTTP_204_NO_CONTENT}
    )
    def delete(self, request, stylist_id):
        stylist = Stylist.objects.get(id=stylist_id)
        stylist.delete()
        return Response(status.HTTP_204_NO_CONTENT)


    @swagger_auto_schema(
        responses = {
            status.HTTP_200_OK : StylistSerializer,
            status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )
    def put(self, request, stylist_id):
        stylist = Stylist.objects.get(id=stylist_id)
    

        serializer = StylistSerializer(stylist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
      
