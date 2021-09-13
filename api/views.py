from .serializers import BasicImageSerializer, PremiumImageSerializer, UploadImageSerializer
from .models import Account, Image
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions


from rest_framework import generics  

class UploadImages(generics.CreateAPIView):
    "API for getting the training data"

    serializer_class = UploadImageSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        account = Account.objects.get(user=self.request.user)
        serializer.save(owner=account)

class DisplayImages(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
  
    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        return Image.objects.filter(owner=account )
    
    def get_serializer_class(self):
        account = Account.objects.get(user=self.request.user)
        if account.tier.tier_name == 'Basic':
            return BasicImageSerializer
        elif account.tier.tier_name == 'Premium':
            return PremiumImageSerializer



