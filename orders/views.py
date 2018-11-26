from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# local imports
from .models import Order, OrderSerializer

class OrdersView(APIView):
    """
    get:
    Return a list of all existing orders

    get: <id> 
    Return order with embeddeded image object

    post:
    Create a new order, along with create embeded image object 
    
    put:
    Update a order
    
    delete:
    Delete the specified order along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : OrderSerializer(many=True)}
    )
    def get(self, request, order_id=None):

        if order_id is not None:
            order = Order.objects.get(id=order_id)
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=OrderSerializer,
        responses={
            status.HTTP_200_OK : OrderSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, order_id):
        
        order = Order.objects.get(id=order_id)
        order.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : OrderSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, order_id):
        
        order = Order.objects.get(id=order_id)
        
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
 