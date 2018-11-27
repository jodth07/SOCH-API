import jwt 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.signals import user_logged_in

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Local imports
from .models import User, UserSerializer
from .models import Address, AddressSerializer
from soch import settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER



# Users CRUD
class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
 
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_200_OK : UserSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
    )
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        # serializer.cart = CartSerializer(data=user['cart'])
        # serializer.purchased = CartSerializer(data=user['purchased'])
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
 
    try:
        email = request.data['email']
        password = request.data['password']
 
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
 
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
 
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
 
    @swagger_auto_schema(
        responses = {status.HTTP_200_OK : UserSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        responses = {
            status.HTTP_200_OK : UserSerializer,
            status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )
    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
 
        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
 
        return Response(serializer.data, status=status.HTTP_200_OK)



class AddressView(APIView):
    """
    get:
    Return a list of all existing addresss

    get: <id> 
    Return address with embeddeded image object

    post:
    Create a new address, along with create embeded image object 
    
    put:
    Update a address
    
    delete:
    Delete the specified address along with its embedded image object
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : AddressSerializer(many=True)}
    )
    def get(self, request, _id=None):

        if _id is not None:
            address = Address.objects.filter(user=_id)
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)
        else:
            addresss = Address.objects.all()
            serializer = AddressSerializer(addresss, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=AddressSerializer,
        responses={
            status.HTTP_200_OK : AddressSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, _id):
        
        address = Address.objects.get(id=_id)
        address.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : AddressSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, _id):
        
        address = Address.objects.get(id=_id)
        
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
  
