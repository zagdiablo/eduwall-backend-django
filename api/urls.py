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
    path("get_materi_data/", views.get_materi_data, name="get_materi_data"),
    path("get_dosen_data/", views.get_dosen_data, name="get_dosen_data"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
