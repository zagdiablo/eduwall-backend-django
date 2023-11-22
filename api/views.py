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


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def edit_profile_data(request):
    """
    accept:
    nama_lengkap

    return http_200_ok
    """

    account_data = get_object_or_404(portal_models.Role, user=request.user)
    nama_lengkap = request.data["nama_lengkap"]

    if nama_lengkap:
        account_data.nama_lengkap = nama_lengkap
    account_data.save()

    return Response({"status": "berhasil mengedit profile"}, status=status.HTTP_200_OK)


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
def get_mata_kuliah_data(request):
    """
    return all_matkul in kelas data <id>
    """

    account_data = get_object_or_404(portal_models.Role, user=request.user)
    kelas_data = get_object_or_404(portal_models.Kelas, id=account_data.kelas_id)

    serializer = serializers.KelasSerializer(kelas_data)
    return Response({"all_matkul": serializer.data}, status=status.HTTP_200_OK)


# get matkul detail
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_detail_mata_kuliah(request, matkul_id):
    matkul = get_object_or_404(portal_models.Matkul, pk=matkul_id)
    materi = get_list_or_404(portal_models.Materi, matkul=matkul)

    serializer = serializers.MateriSerializer(materi, many=True)
    return Response({"materi": serializer.data}, status=status.HTTP_200_OK)


# get konten materi
@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_materi_data(request):
    """
    accept:
    materi_id

    return:
    "materi": {
        "id": 2,
        "judul_materi"
        "url_video"
        "video_text_transcript"
        "file_materi"
        "link_materi"
        "matkul"
        "dosen_pembuat"
    }
    """

    mater_konten = get_object_or_404(portal_models.Materi, pk=request.data["materi_id"])
    serializer = serializers.MateriSerializer(mater_konten)
    return Response({"materi": serializer.data}, status=status.HTTP_200_OK)


# get dosen id
@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_dosen_data(request):
    """
    accept:
    dosen_id

    return:
    "dosen_data": {
        "id"
        "kelas"
        "nama_lengkap"
        "role"
        "nim"
        "nid"
    """

    dosen = get_object_or_404(portal_models.Role, pk=request.data["dosen_id"])
    if dosen.role != "DOSEN":
        return Response({"status": "No Such Dosen"}, status=status.HTTP_404_NOT_FOUND)

    serialzer = serializers.RoleSerializer(dosen)
    return Response({"dosen_data": serialzer.data}, status=status.HTTP_200_OK)
