from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserLoginValidateSerializer, UserCreateValidateSerializer, UserConfirmSerializer
from .models import ConfirmationCode
from django.contrib.auth.models import User
import random
from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        return Response(status=status.HTTP_201_CREATED,
                        data={'user_id': user.id})


class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))

        code = ConfirmationCode.objects.create(**serializer.validated_data, code=code)

        if User.objects.filter(user_ptr_id=request.data['user_id'], code=request.data['code']):
            User.objects.update(is_active=True)
            return Response(status=status.HTTP_202_ACCEPTED,
                            data={'code': 'confirmed'})

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'error': 'wrong id or code!'})


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserLoginValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error': 'Username or Password wrong!'})
