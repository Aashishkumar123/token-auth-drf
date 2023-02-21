from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer, StudentSerializer
from .models import Student
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })


class SignupAPIView(APIView):
    """This api will handle signup"""
    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                res = { 'status' : status.HTTP_201_CREATED }
                return Response(res, status = status.HTTP_201_CREATED)
        res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """This api will handle login and generate access and refresh token for authenticate user."""
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        token = Token.objects.get(user=user)
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                    "Token" : token.key
                               }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Email or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)


class StudentAPIView(APIView):
    """This api will handle student"""
    permission_classes = [ IsAuthenticated ]
    def get(self,request):
        data = Student.objects.all()
        serializer = StudentSerializer(data, many = True)
        response = {
                "status": status.HTTP_200_OK,
                "message": "success",
                "data": serializer.data
                }
        return Response(response, status = status.HTTP_200_OK)
