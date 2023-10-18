from django.urls import path
from . import views


app_name = "dosen"


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "delete_materi_matkul/<int:materi_id>/<int:matkul_id>",
        views.delete_materi_matkul,
        name="delete_materi_matkul",
    ),
    path(
        "tambah_materi_matkul/<int:matkul_id>",
        views.tambah_materi_matkul,
        name="tambah_materi_matkul",
    ),
    path(
        "edit_materi_matkul/<int:materi_id>/<int:matkul_id>",
        views.edit_materi_matkul,
        name="edit_materi_matkul",
    ),
    path(
        "tambah_quiz_materi/<int:materi_id>/<int:matkul_id>",
        views.tambah_quiz_materi,
        name="tambah_quiz_materi",
    ),
    path(
        "edit_quiz_materi/<int:materi_id>/<int:matkul_id>/<int:quiz_id>",
        views.edit_quiz_materi,
        name="edit_quiz_materi",
    ),
    path(
        "delete_quiz_materi/<int:materi_id>/<int:matkul_id>/<int:quiz_id>",
        views.delete_quiz_materi,
        name="delete_quiz_materi",
    ),
    path(
        "tambah_soal_quiz/<int:materi_id>/<int:matkul_id>/<int:quiz_id>",
        views.tambah_soal_quiz,
        name="tambah_soal_quiz",
    ),
    path(
        "edit_soal_quiz/<int:materi_id>/<int:matkul_id>/<int:quiz_id>/<int:soal_id>",
        views.edit_soal_quiz,
        name="edit_soal_quiz",
    ),
    path(
        "delete_soal_quiz/<int:materi_id>/<int:matkul_id>/<int:quiz_id>/<int:soal_id>",
        views.delete_soal_quiz,
        name="delete_soal_quiz",
    ),
]
