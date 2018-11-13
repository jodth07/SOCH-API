from django.shortcuts import render
import json
from rest_framework import status, generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer, Group, GroupSerializer, Category, CategorySerializer, Product, ProductSerializer, Style, StyleSerializer, Cart, CartSerializer, Purchased, PurchasedSerializer, User, UserSerializer, Featurette, FeaturetteSerializer, Image, ImageSerializer 
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files import File
import base64
from django.http import HttpResponse
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


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

    permission_classes = (AllowAny,)

    
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
    
    # @swagger_auto_schema(
    #     response={status.HTTP_204_NO_CONTENT}
    #     )
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

    permission_classes = (AllowAny,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

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
        image.name = request.data.get("name")
        image.timestamp = request.data.get("timestamp")
        image.save()
        
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CategoryView (APIView):
    """
    get:
    Return a list of all existing images/medias 
    
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
    responses={ status.HTTP_200_OK : CategorySerializer(many=True)}
    )
    def get(self, request, category_id=None):

        if category_id is not None:
            category = Category.objects.get(id=category_id)
            serializer = CategorySerializer(category, many=False)
            return Response(serializer.data)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)


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
    """
    get:
    Return a list of all existing contacts 
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : CartSerializer(many=True)}
    )
    def get(self, request, cart_id=None):

        if cart_id is not None:
            cart = Cart.objects.get(id=cart_id)
            serializer = CartSerializer(cart, many=False)
            return Response(serializer.data)
        else:
            cart = Cart.objects.all()
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)


class PurchasedView (generics.ListCreateAPIView):
    """
    get:
    Return a list of all existing contacts 
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : PurchasedSerializer(many=True)}
    )
    def get(self, request, purchased_id=None):

        if purchased_id is not None:
            purchases = Purchased.objects.get(id=purchased_id)
            serializer = PurchasedSerializer(purchases, many=False)
            return Response(serializer.data)
        else:
            purchases = Purchased.objects.all()
            serializer = PurchasedSerializer(purchases, many=True)
            return Response(serializer.data)
    

class UsersView(APIView):
    permission_classes = (IsAuthenticated, )
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

    # permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : UserSerializer(many=True)}
    )
    def get(self, request, user_id=None):

        if user_id is not None:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
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


class FeaturetteView (APIView):
    """
    get:
    Return a list of all existing contacts 
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : FeaturetteSerializer(many=True)}
    )
    def get(self, request, feat_id=None):

        if feat_id is not None:
            feat = Featurette.objects.get(id=feat_id)
            serializer = FeaturetteSerializer(feat, many=False)
            return Response(serializer.data)
        else:
            feat_id = 1
            feat = Featurette.objects.get(id=feat_id)
            serializer = FeaturetteSerializer(feat, many=False)
            return Response(serializer.data)

    