from rest_framework import serializers
from django.contrib.auth.models import User

from portal import models as portal_models


class UserSeralizer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "email", "password"]


class RoleSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.Role
        fields = ["id", "kelas", "nama_lengkap", "role", "nim", "nid"]


class KelasSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.Kelas
        fields = ["id", "kode_kelas", "daftar_matkul"]


# get matkul data
class MatkulSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.Matkul
        fields = ["id", "judul_matkul", "dosen_pengampu"]


# get quiz data per materi
class MateriQuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = portal_models.Quiz
        fields = "__all__"


# get materi data
class MateriSerializer(serializers.ModelSerializer):
    quiz = MateriQuizesSerializer(source="materi_quiz", many=True)

    class Meta(object):
        model = portal_models.Materi
        fields = [
            "id",
            "judul_materi",
            "url_video",
            "video_text_transcript",
            "file_materi",
            "link_materi",
            "matkul",
            "dosen_pembuat",
            "quiz",
        ]


# get quiz
class QuizSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.Quiz
        fields = [
            "id",
            "judul_quiz",
            "waktu_pengerjaan",
            "materi",
            "dibuat_oleh",
        ]


# get jawaban quiz
class SoalSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.Soal
        fields = [
            "text_soal",
            "jawaban_a",
            "jawaban_b",
            "jawaban_c",
            "jawaban_d",
            "jawaban_benar",
            "quiz",
        ]


# get nilai (jika ada)
class RiwayatPengerjaanSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.RiwayatPengerjaanQuiz
        fields = ["quiz", "mahasiswa", "tanggal_pengerjaan", "nilai"]


class NilaiQuizSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = portal_models.RiwayatPengerjaanQuiz
        fields = ["quiz", "tanggal_pengerjaan", "nilai"]
