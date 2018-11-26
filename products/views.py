from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Product, ProductSerializer
from .models import Variation, VariationSerializer

class StyleListView(APIView):
    """
    get:
    Return a list of all existing products
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ProductSerializer(many=True)}
    )
    def get(self, request):
        products = Product.objects.filter(category="Style")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


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
            products = Product.objects.filter(category="Product")
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
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, product_id):
        
        product = Product.objects.get(id=product_id)
        product.delete()
        
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
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

class VariationsView(APIView):
    """
    get:
    Return a list of all existing variations

    get: <id> 
    Return variation with embeddeded image object

    post:
    Create a new variation, along with create embeded image object 
    
    put:
    Update a variation
    
    delete:
    Delete the specified variation along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : VariationSerializer(many=True)}
    )
    def get(self, request, variation_id=None):

        if variation_id is not None:
            variation = Variation.objects.get(id=variation_id)
            serializer = VariationSerializer(variation, many=False)
            return Response(serializer.data)
        else:
            variations = Variation.objects.all()
            serializer = VariationSerializer(variations, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=VariationSerializer,
        responses={
            status.HTTP_200_OK : VariationSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = VariationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, variation_id):
        
        variation = Variation.objects.get(id=variation_id)
        variation.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : VariationSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, variation_id):
        
        variation = Variation.objects.get(id=variation_id)
        
        serializer = VariationSerializer(variation, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 