from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = "api"


urlpatterns = [
    path("api_login/", views.api_login, name="api_login"),
    path("test_token/", views.api_test_token, name="test_token"),
    path("get_role_data/", views.get_role_data, name="get_role_data"),
    path("get_kelas_data/", views.get_kelas_data, name="get_kelas_data"),
    path("edit_profile_data/", views.edit_profile_data, name="edit_profile_data"),
    path(
        "get_mata_kuliah_data/", views.get_mata_kuliah_data, name="get_mata_kuliah_data"
    ),
    path(
        "get_detail_mata_kuliah/<int:matkul_id>",
        views.get_detail_mata_kuliah,
        name="get_detail_mata_kuliah",
    ),
    path("get_quiz_data/<int:materi_id>", views.get_quiz_data, name="get_quiz_data"),
    path("get_quiz_soal/<int:quiz_id>", views.get_quiz_soal, name="get_quiz_soal"),
    path(
        "get_quiz_per_materi/<int:materi_id>",
        views.get_quiz_per_materi,
        name="get_quiz_per_materi",
    ),
    path("get_dosen_data/", views.get_dosen_data, name="get_dosen_data"),
    path("get_quiz_nilai/<int:quiz_id>", views.get_quiz_nilai, name="get_quiz_nilai"),
    path("post_quiz_nilai/", views.post_quiz_nilai, name="post_quiz_nilai"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
