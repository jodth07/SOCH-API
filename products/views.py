from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Product, ProductSerializer
from images.models import Image

class ProductsView(APIView):
    """
    get:
    Return a list of all existing products

    get: <id> 
    Return product with embeddeded image object

    post:
    Create a new product, along with create embeded image object 
    
    put:
    Update a product
    
    delete:
    Delete the specified product along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ProductSerializer(many=True)}
    )
    def get(self, request, product_id=None):

        if product_id is not None:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductSerializer,
        responses={
            status.HTTP_200_OK : ProductSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, product_id):
        
        product = Product.objects.get(id=product_id)
        image = Image.objects.get(id=product.image.id)
        image.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : ProductSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, product_id):
        
        product = Product.objects.get(id=product_id)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 