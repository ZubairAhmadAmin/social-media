from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics

from accounts.serializers import RegisterSerializer


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    
    Queryset = User
    serializer_class = RegisterSerializer
