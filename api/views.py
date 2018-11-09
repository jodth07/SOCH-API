from django.shortcuts import render
import json
from rest_framework import status, generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer, Group, GroupSerializer, Category, CategorySerializer, Product, ProductSerializer, Style, StyleSerializer, Cart, CartSerializer, Purchased, PurchasedSerializer, User, UserSerializer, Featurette, FeaturetteSerializer 
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ContactsView(APIView):
    """
    get:
    Return a list of all existing contacts 
    
    post:
    Create a new contact 
    
    put:
    Update a contact
    
    delete:
    Delete a contact
    """
    
    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ContactSerializer(many=True)}
    )
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
            
    @swagger_auto_schema(
        request_body=ContactSerializer,
        responses={
            status.HTTP_200_OK : ContactSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : ContactSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, contact_id):
        
         contact = Contact.objects.get(id=contact_id)
         contact.first_name = request.data.get("first_name")
         contact.last_name = request.data.get("last_name")
         contact.email = request.data.get("email")
         contact.phone = request.data.get("phone")
         contact.address = request.data.get("address")
         contact.save()
        
         serializer = ContactSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            

class GroupView (generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class CategoryView (generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsView(APIView):
    """
    get:
    Return a list of all existing products 
    
    post:
    Create a new product 
    
    put:
    Update a product
    
    delete:
    Delete a product
    """
    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ProductSerializer(many=True)}
    )
    def get(self, request, product_id=None):
        if product_id is not None:
            product = Product.objects.get(id=product_id)
            serializer = ProductSerializer(product, many=True)
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
    def delete(self, request, contact_id):
        
        product = Product.objects.get(id=contact_id)
        product.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : ProductSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, contact_id):
        
        product = Contact.objects.get(id=contact_id)
        product.name = request.data.get("name")
        product.price = request.data.get("price")
        product.image = request.data.get("image") # may need to be wrapped.
        product.company = request.data.get("company")
        product.description = request.data.get("description")
        product.quantity = request.data.get("quantity")
        product.num_requested = request.data.get("num_requested")
        product.created_date = request.data.get("created_date")
        product.purchased_date = request.data.get("purchased_date")
        product.categories = request.data.get("categories")
    
        product.save()
    
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    
class StylesView(APIView):
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
    @swagger_auto_schema(
        responses = {status.HTTP_200_OK : StyleSerializer(many=True)}
    )
    def get(self, request, style_id=None):
        if style_id is not None:
            style = Style.objects.get(id=style_id)
            serializer = StyleSerializer(style, many=True)
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
        s_serializer = StyleSerializer(data=request.data)
        if s_serializer.is_valid():
            s_serializer.save()
            return Response(s_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(s_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        response = {status.HTTP_204_NO_CONTENT}
    )
    def delete(self, request, style_id):
        style = Style.objects.get(id=style_id)
        style.delete()
        return Response(status.HTTP_204_NO_CONTENT)


    @swagger_auto_schema(
        responses = {
            status.HTTP_200_OK : StyleSerializer,
            status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )
    def put(self, request, style_id):
        style = Style.objects.get(id=style_id)
        style.name = request.data.get("name")
        style.price = request.data.get("price")
        style.description = request.data.get("description")
        style.num_requested = request.data.get("num_requested")
        style.image = request.data.get("image")
        style.duration = request.data.get("duration")
        style.created_date = request.data.get("created_date")
        style.purchased_date = request.data.get("purchased_date")
        style.categories = request.data.get("categories")
        style.save()

        serializer = StyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
      

class CartView (generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = GroupSerializer


class PurchasedView (generics.ListCreateAPIView):
    queryset = Purchased.objects.all()
    serializer_class = GroupSerializer
    

class UsersView(APIView):
    """
    get:
    Return a list of all existing users 
    
    post:
    Create a new user 
    
    put:
    Update a user
    
    delete:
    Delete a user
    """
    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : UserSerializer(many=True)}
    )
    def get(self, request, user_id=None):

        if contact_id is not None:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            users = Contact.objects.all()
            serializer = ContactSerializer(users, many=True)
            return Response(serializer.data)
            
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            status.HTTP_200_OK : UserSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
    def post(self, request):
            
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
    def delete(self, request, user_id):
        
        user = User.objects.get(id=user_id)
        user.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : UserSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    ) 
    def put (self, request, user_id):
        
        user = User.objects.get(id=user_id)
        user.image = request.data.get("image")
        user.first_name = request.data.get("first_name")
        user.last_name = request.data.get("last_name")
        user.username = request.data.get("username")
        user.password = request.data.get("password")
        user.email = request.data.get("email")
        user.phone = request.data.get("phone")
        user.address = request.data.get("address")
        user.city = request.data.get("city")
        user.state = request.data.get("state")
        user.zipcode = request.data.get("zipcode")
        user.stylist = request.data.get("stylist")
        user.cart = request.data.get("cart")
        user.purchased = request.data.get("purchased")
        user.save()

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)    


class FeaturetteView (generics.ListCreateAPIView):
    queryset = Featurette.objects.all()
    serializer_class = GroupSerializer
    