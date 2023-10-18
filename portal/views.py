from django.shortcuts import render, redirect, get_object_or_404
from . import models


# Create your views here.
def test_redirect(request):
    if request.user.is_authenticated:
        return redirect("dashboard_redirect/")

    return redirect("login/", {"site_title": "Login"})


def dashboard_redirect(request):
    account_data = models.Role.objects.filter(user_id=request.user.id).first()

    print(account_data.role)

    if account_data:
        if account_data.role == "MAHASISWA":
            return redirect("mahasiswa:dashboard")
        if account_data.role == "DOSEN":
            return redirect("dosen:dashboard")

    return redirect("portal:login")
