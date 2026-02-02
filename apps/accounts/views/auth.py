from rest_framework.views import viewsets
from rest_framework.response import Response
from serializers.auth import LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(viewsets.ViewSet):
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(email=serializer.validated_data['email'],password=serializer.validated_data['password'])
            if user is not None:
                refresh=RefreshToken.for_user(user)
                return Response({
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                })
            else:
                return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogoutView(viewsets.ViewSet):
    def post(self, request):
        try:
            refresh_token=request.data['refresh']
            token=RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':'Logout successful'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)



class RegisterView(viewsets.ViewSet):
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({'message':'User created successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

