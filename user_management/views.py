from django.shortcuts import render
from .models import UserInfo
from rest_framework import generics
from .serializers import UserSerializer


class UserProfileCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = UserInfo.objects.all(),
    serializer_class = UserSerializer