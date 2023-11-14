from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = "api"


urlpatterns = [
    path("api_login/", views.api_login, name="api_login"),
    path("test_token/", views.api_test_token, name="test_token"),
    path("get_role_data/", views.get_role_data, name="get_role_data"),
    path("get_kelas_data/", views.get_kelas_data, name="get_kelas_data"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
