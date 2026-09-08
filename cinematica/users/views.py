from .serializers import UserRegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(['POST'])
def authorization_api_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def registration_api_view(request):
    # step 0: validation
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # step 1: receive data
    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    # step 2: create user
    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=True
    )

    # step 3: return response
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id})