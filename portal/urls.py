from django.urls import path
from django.contrib.auth import views as auth_views
from . import forms
from . import views

app_name = "portal"


urlpatterns = [
    path("", views.test_redirect, name="test_redirect"),
    path("dashboard_redirect/", views.dashboard_redirect, name="dashboard_redirect"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="public/login.html", authentication_form=forms.LoginForm
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
