from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Cart, CartItemSerializer, CartSerializer, CartItem



class CartsView(APIView):
    """
    get:
    Return a list of all existing carts

    get: <id> 
    Return cart with embeddeded image object

    post:
    Create a new cart, along with create embeded image object 
    
    put:
    Update a cart
    
    delete:
    Delete the specified cart along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : CartSerializer(many=True)}
    )
    def get(self, request, _id=None):

        if _id is not None:
            # cart = Cart.objects.filter(user=_id, purchased=False)
            cart = Cart.objects.get(user=_id, purchased=False)
            serializer = CartSerializer(cart, many=False)
            return Response(serializer.data)
        else:
            carts = Cart.objects.all()
            serializer = CartSerializer(carts, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CartSerializer,
        responses={
            status.HTTP_200_OK : CartSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, _id):
        
        cart = Cart.objects.get(id=_id)
        cart.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : CartSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, _id):
        
        cart = Cart.objects.get(id=_id)
        
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 
class CartItemsView(APIView):
    """
    get:
    Return a list of all existing cart_items

    get: <id> 
    Return cart_item with embeddeded image object

    post:
    Create a new cart_item, along with create embeded image object 
    
    put:
    Update a cart_item
    
    delete:
    Delete the specified cart_item along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : CartItemSerializer(many=True)}
    )
    def get(self, request, cart_item_id=None):

        if cart_item_id is not None:
            cart_item = CartItem.objects.get(id=cart_item_id)
            serializer = CartItemSerializer(cart_item, many=False)
            return Response(serializer.data)
        else:
            cart_items = CartItem.objects.all()
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CartItemSerializer,
        responses={
            status.HTTP_200_OK : CartItemSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, cart_item_id):
        
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : CartItemSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, cart_item_id):
        
        cart_item = CartItem.objects.get(id=cart_item_id)
        
        serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 