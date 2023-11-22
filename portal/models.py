from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)


ROLE = [
    ("MAHASISWA", "MAHASISWA"),
    ("DOSEN", "DOSEN"),
]


# test API Models
class TestAPI(TimeStampedModel, ActivatorModel, TitleDescriptionModel, models.Model):
    class Meta:
        verbose_name_plural = "Test API stuff"

    email = models.EmailField(verbose_name="Email")

    def __str__(self) -> str:
        return self.title


# Create your models here.
class Role(models.Model):
    kelas = models.ForeignKey(
        "Kelas",
        related_name="kelas",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    nama_lengkap = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name="data_user", null=True, blank=True, on_delete=models.CASCADE
    )
    role = models.CharField(max_length=20, choices=ROLE)

    # if dosen
    nid = models.CharField(max_length=50, blank=True, null=True)
    matkul_diajar = models.ManyToManyField("Matkul", blank=True)
    # if mahasiswa
    nim = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ("nama_lengkap",)
        verbose_name_plural = "Data User"

    def __str__(self) -> str:
        return str(self.nama_lengkap) + "|" + str(self.role)


class Matkul(models.Model):
    judul_matkul = models.CharField(max_length=200)
    dosen_pengampu = models.ForeignKey(
        "Role", related_name="materi_diajar", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("judul_matkul",)
        verbose_name_plural = "List Mata Kuliah"

    def __str__(self) -> str:
        return str(self.judul_matkul) + " | " + str(self.dosen_pengampu)


class Materi(models.Model):
    judul_materi = models.CharField(max_length=200)
    url_video = models.CharField(max_length=200, blank=True, null=True)
    video_text_transcript = models.TextField(blank=True, null=True)
    file_materi = models.FileField(upload_to="dokumen_materi", blank=True, null=True)
    link_materi = models.CharField(max_length=1000, null=True, blank=True, default="")
    matkul = models.ForeignKey(
        "Matkul",
        related_name="materi_matkul",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    dosen_pembuat = models.ForeignKey(
        "Role",
        related_name="dosen_pengajar",
        on_delete=models.CASCADE,
        limit_choices_to={"role": "DOSEN"},
    )

    class Meta:
        ordering = ("judul_materi",)
        verbose_name_plural = "List Materi"

    def __str__(self) -> str:
        return self.judul_materi


class Quiz(models.Model):
    judul_quiz = models.CharField(max_length=200)
    waktu_pengerjaan = models.IntegerField()
    materi = models.ForeignKey(
        "Materi",
        related_name="materi_quiz",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    dibuat_oleh = models.ForeignKey(
        "Role",
        related_name="dosen_pembuat",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        limit_choices_to={"role": "DOSEN"},
    )

    class Meta:
        ordering = ("judul_quiz",)
        verbose_name_plural = "List Quiz"

    def __str__(self) -> str:
        return self.judul_quiz


class Soal(models.Model):
    text_soal = models.TextField(blank=False, null=False)
    jawaban_a = models.CharField(max_length=200, null=True)
    jawaban_b = models.CharField(max_length=200, null=True)
    jawaban_c = models.CharField(max_length=200, null=True)
    jawaban_d = models.CharField(max_length=200, null=True)
    jawaban_benar = models.CharField(max_length=1)
    quiz = models.ForeignKey("Quiz", related_name="soal_quiz", on_delete=models.CASCADE)

    class Meta:
        ordering = ("quiz_id",)
        verbose_name_plural = "List Soal"

    def __str__(self) -> str:
        return "quiz " + str(self.quiz)


class RiwayatPengerjaanQuiz(models.Model):
    quiz = models.ForeignKey(
        "Quiz", related_name="quiz_terkait", on_delete=models.DO_NOTHING
    )
    mahasiswa = models.ForeignKey(
        "Role",
        related_name="quiz_dikerjakan",
        on_delete=models.DO_NOTHING,
        limit_choices_to={"role": "MAHASISWA"},
    )
    tanggal_pengerjaan = models.DateTimeField(auto_now_add=True)
    nilai = models.FloatField()

    class Meta:
        ordering = ("mahasiswa_id",)
        verbose_name_plural = "Riwayat Pengerjaan Quiz"

    def __str__(self) -> str:
        return str(self.mahasiswa) + " " + str(self.quiz)


class Kelas(models.Model):
    kode_kelas = models.CharField(max_length=200)
    daftar_matkul = models.ManyToManyField("Matkul", blank=True)

    class Meta:
        ordering = ("kode_kelas",)
        verbose_name_plural = "Daftar Kelas"

    def __str__(self) -> str:
        return self.kode_kelas
