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
    daftar_matkul = []
    for index, matkul_id in enumerate(serializer.data["daftar_matkul"]):
        daftar_matkul.append(
            {
                "id": matkul_id,
                "nama_matkul": portal_models.Matkul.objects.get(
                    pk=matkul_id
                ).judul_matkul,
            }
        )

    return Response(
        {"all_matkul": serializer.data, "daftar_matkul": daftar_matkul},
        status=status.HTTP_200_OK,
    )


# get matkul detail
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_detail_mata_kuliah(request, matkul_id):
    matkul = get_object_or_404(portal_models.Matkul, pk=matkul_id)
    materi = get_list_or_404(portal_models.Materi, matkul=matkul)

    serializer = serializers.MateriSerializer(materi, many=True)
    return Response({"materi": serializer.data}, status=status.HTTP_200_OK)


# get quiz data
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_quiz_data(request, materi_id):
    materi = get_object_or_404(portal_models.Materi, pk=materi_id)
    quiz = get_list_or_404(portal_models.Quiz, materi=materi)

    serializer = serializers.QuizSerializer(quiz, many=True)
    return Response(
        {"quiz": serializer.data},
        status=status.HTTP_200_OK,
    )


# get soal quiz
@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_quiz_soal(request, quiz_id):
    quiz = get_object_or_404(portal_models.Quiz, pk=quiz_id)
    soal_quiz = get_list_or_404(portal_models.Soal, quiz=quiz)
    soal_quiz_serializer = serializers.SoalSerializer(soal_quiz, many=True)

    quiz_format = {}
    quiz_format["id"] = quiz.id
    quiz_format["nama_quiz"] = quiz.judul_quiz
    quiz_format[""]
    for index, _ in enumerate(soal_quiz):
        jawaban_format = []
        jawaban = {
            "a": soal_quiz_serializer.data[index]["jawaban_a"],
            "b": soal_quiz_serializer.data[index]["jawaban_b"],
            "c": soal_quiz_serializer.data[index]["jawaban_c"],
            "d": soal_quiz_serializer.data[index]["jawaban_d"],
        }
        jawaban_format.append(
            jawaban[soal_quiz_serializer.data[index]["jawaban_benar"]]
        )
        for chr in "abcd":
            if chr != soal_quiz_serializer.data[index]["jawaban_benar"]:
                jawaban_format.append(jawaban[chr])

        quiz_format.append(
            {
                "text": soal_quiz_serializer.data[0]["text_soal"],
                "answer": [jawaban_format],
            },
        )

    # print(soal_quiz_serializer.data[0]["text_soal"])
    print(quiz_format)
    return Response({"soal_quiz": quiz_format}, status=status.HTTP_200_OK)


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


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def post_quiz_nilai(request):
    """
    accept: quiz_id, nilai

    return status success or failed
    """
    account_data = get_object_or_404(portal_models.Role, user=request.user)
    quiz = get_object_or_404(portal_models.Quiz, pk=request.data["quiz_id"])

    if quiz:
        new_riwayat_pengerjaan = portal_models.RiwayatPengerjaanQuiz(
            quiz=quiz, mahasiswa=account_data, nilai=request.data["nilai"]
        )
        new_riwayat_pengerjaan.save()
        return Response({"status": "Success"}, status=status.HTTP_200_OK)
    return Response({"statuse": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_quiz_nilai(request, quiz_id):
    riwayat = get_object_or_404(portal_models.RiwayatPengerjaanQuiz, quiz=quiz_id)
    serializer = serializers.NilaiQuizSerializer(riwayat)
    return Response({"quiz_nilai": serializer.data}, status=status.HTTP_200_OK)
