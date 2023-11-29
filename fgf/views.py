from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def login(request):
    try:
        user = get_object_or_404(User, username=request.data.get("username"))
        password = request.data.get("password")

        if not password:
            raise ValueError("Password is missing in the request.")

        if not user.check_password(password):
            raise ValueError("Incorrect password.")

        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data})
    except User.DoesNotExist:
        return Response(
            {"detail": "User not found."}, status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        username = request.data.get("username")

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return Response(
                {"detail": "Username already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Continue with user creation
        serializer.save()
        user = User.objects.get(username=username)
        user.set_password(request.data["password"])
        user.save()

        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email))
