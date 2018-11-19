from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status #, generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Featurette, FeaturetteSerializer

# Create your views here.

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

    