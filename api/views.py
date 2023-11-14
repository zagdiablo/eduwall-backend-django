from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from portal import models as portal_models
from . import models
from . import serializers


@api_view(["POST"])
def api_login(request):
    user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response({"detail": "Not Found."}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = serializers.UserSeralizer(instance=user)
    return Response(
        {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def api_test_token(request):
    return Response(f"Passed for {request.user.username}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_role_data(request):
    role = get_object_or_404(portal_models.Role, user=request.user)
    serializer = serializers.RoleSerializer(role)
    return Response({"role": serializer.data}, status=status.HTTP_200_OK)


# get kelas data
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_kelas_data(request):
    kelas = portal_models.Kelas.objects.all()
    serializer = serializers.KelasSerializer(kelas, many=True)
    return Response({"kelas": serializer.data}, status=status.HTTP_200_OK)


# get matkul data
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_kelas_data(request):
    kelas = portal_models.Kelas.objects.all()
    serializer = serializers.KelasSerializer(kelas, many=True)
    return Response({"kelas": serializer.data}, status=status.HTTP_200_OK)
# get materi data
# get module
# get quiz
# get nilai (jika ada)
