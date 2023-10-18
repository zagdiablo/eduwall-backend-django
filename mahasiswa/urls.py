from django.urls import path
from . import views


app_name = "mahasiswa"


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("list_mata_kuliah", views.list_mata_kuliah, name="list_mata_kuliah"),
    path("list_materi/<int:matkul_id>", views.list_materi, name="list_materi"),
    path("konten_materi/<int:materi_id>", views.konten_materi, name="konten_materi"),
    path("modul_materi/<int:materi_id>", views.modul_materi, name="modul_materi"),
    path("quiz_materi/<int:materi_id>", views.quiz_materi, name="quiz_materi"),
    path("play_quiz/<int:materi_id>/<int:quiz_id>", views.play_quiz, name="play_quiz"),
    path("nilai_quiz/<int:materi_id>", views.nilai_quiz, name="nilai_quiz"),
]
