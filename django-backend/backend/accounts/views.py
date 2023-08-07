from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, LoginSerializer
from accounts.tokenauthentication import JWTAuthentication

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        token = JWTAuthentication.generate_token(payload=serializer.data)
        return Response(
            {
                "message": 'login successfull',
                "token": token,
                'user': serializer.data
            }, status=status.HTTP_201_CREATED 
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
