from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from .modules.get_youtube_video_transcript import get_transcript
from portal import models


# Create your views here.
@login_required
def dashboard(request):
    account_data = get_object_or_404(models.Role, user_id=request.user.id)
    all_matkul_diajar = models.Matkul.objects.filter(dosen_pengampu=account_data.id)

    if account_data:
        return render(
            request,
            "dashboard_dosen.html",
            {
                "site_title": "Dashboard Dosen",
                "account_data": account_data,
                "all_matkul_diajar": all_matkul_diajar,
            },
        )

    return redirect("portal:logout")


@login_required
def tambah_materi_matkul(request, matkul_id):
    matkul = get_object_or_404(models.Matkul, id=matkul_id)
    account_data = get_object_or_404(models.Role, user_id=request.user.id)
    all_materi = models.Materi.objects.filter(
        matkul_id=matkul_id, dosen_pembuat=account_data.id
    )

    if request.method == "POST":
        form = forms.EditMateriForm(request.POST)
        if form.is_valid():
            materi = form.save(commit=False)
            materi.matkul = matkul
            materi.dosen_pembuat = account_data
            video_url = form.cleaned_data["url_video"]
            materi.video_text_transcript = get_transcript(video_url)
            materi.save()
            return redirect("dosen:tambah_materi_matkul", matkul_id)
    else:
        form = forms.EditMateriForm()

        return render(
            request,
            "tambah_materi_dosen.html",
            {
                "matkul": matkul,
                "account_data": account_data,
                "all_materi": all_materi,
                "form": form,
            },
        )


@login_required
def edit_materi_matkul(request, materi_id, matkul_id):
    materi = get_object_or_404(models.Materi, pk=materi_id)
    account_data = get_object_or_404(models.Role, user=request.user)
    matkul = get_object_or_404(models.Matkul, id=matkul_id)
    all_quiz_materi = models.Quiz.objects.filter(materi=materi)

    if request.method == "POST":
        form = forms.EditMateriForm(request.POST, request.FILES, instance=materi)
        if form.is_valid():
            materi = form.save(commit=False)
            materi.dosen_pembuat = account_data
            materi.matkul = matkul
            video_url = form.cleaned_data["url_video"]
            materi.video_text_transcript = get_transcript(video_url)
            materi.save()
            return redirect("dosen:tambah_materi_matkul", matkul_id)
    else:
        form = forms.EditMateriForm()

    return render(
        request,
        "edit_materi_dosen.html",
        {
            "materi": materi,
            "form": form,
            "matkul": matkul,
            "all_quiz_materi": all_quiz_materi,
        },
    )


@login_required
def delete_materi_matkul(request, materi_id, matkul_id):
    materi = get_object_or_404(models.Materi, pk=materi_id)
    materi.delete()

    return redirect("dosen:tambah_materi_matkul", matkul_id)


@login_required
def tambah_quiz_materi(request, materi_id, matkul_id):
    matkul = get_object_or_404(models.Matkul, pk=matkul_id)
    materi = get_object_or_404(models.Materi, pk=materi_id)
    account_data = get_object_or_404(models.Role, user=request.user)

    if request.method == "POST":
        form = forms.EditQuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.materi = materi
            quiz.dibuat_oleh = account_data
            quiz.save()
            return redirect("dosen:edit_materi_matkul", materi_id, matkul_id)
    else:
        form = forms.EditQuizForm()

    return render(
        request,
        "tambah_quiz_dosen.html",
        {
            "materi": materi,
            "account_data": account_data,
            "matkul": matkul,
            "form": form,
        },
    )


@login_required
def edit_quiz_materi(request, materi_id, matkul_id, quiz_id):
    matkul = get_object_or_404(models.Matkul, pk=matkul_id)
    materi = get_object_or_404(models.Materi, pk=materi_id)
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    account_data = get_object_or_404(models.Role, user=request.user)
    all_soal = models.Soal.objects.filter(quiz=quiz)

    if request.method == "POST":
        form = forms.EditQuizForm(request.POST, instance=quiz)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.matkul = matkul
            quiz.dosen_pembuat = account_data
            quiz.save()
            return redirect("dosen:edit_quiz_materi", materi_id, matkul_id, quiz_id)
    else:
        form = forms.EditQuizForm()

    return render(
        request,
        "edit_quiz_dosen.html",
        {
            "matkul": matkul,
            "materi": materi,
            "quiz": quiz,
            "form": form,
            "all_soal": all_soal,
        },
    )


@login_required
def delete_quiz_materi(request, materi_id, matkul_id, quiz_id):
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    quiz.delete()

    return redirect("dosen:edit_materi_matkul", materi_id, matkul_id)


@login_required
def tambah_soal_quiz(request, materi_id, matkul_id, quiz_id):
    matkul = get_object_or_404(models.Matkul, pk=matkul_id)
    materi = get_object_or_404(models.Materi, pk=materi_id)
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    account_data = get_object_or_404(models.Role, user=request.user)

    if request.method == "POST":
        form = forms.EditSoalForm(request.POST)
        if form.is_valid():
            soal = form.save(commit=False)
            soal.quiz = quiz
            soal.save()
            return redirect("dosen:tambah_soal_quiz", materi.id, matkul.id, quiz.id)
    else:
        form = forms.EditSoalForm()

    return render(
        request,
        "tambah_soal_dosen.html",
        {
            "matkul": matkul,
            "materi": materi,
            "quiz": quiz,
            "account_data": account_data,
            "form": form,
        },
    )


@login_required
def edit_soal_quiz(request, materi_id, matkul_id, quiz_id, soal_id):
    matkul = get_object_or_404(models.Matkul, pk=matkul_id)
    materi = get_object_or_404(models.Materi, pk=materi_id)
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    soal = get_object_or_404(models.Soal, pk=soal_id)
    account_data = get_object_or_404(models.Role, user=request.user)

    if request.method == "POST":
        form = forms.EditSoalForm(request.POST, instance=soal)
        if form.is_valid():
            soal = form.save(commit=False)
            soal.quiz = quiz
            soal.save()
            return redirect("dosen:edit_quiz_materi", materi.id, matkul.id, quiz.id)
    else:
        form = forms.EditSoalForm()

    return render(
        request,
        "edit_soal_dosen.html",
        {
            "matkul": matkul,
            "materi": materi,
            "quiz": quiz,
            "account_data": account_data,
            "form": form,
            "soal": soal,
        },
    )


@login_required
def delete_soal_quiz(request, materi_id, matkul_id, quiz_id, soal_id):
    to_delete_soal = get_object_or_404(models.Soal, pk=soal_id)
    to_delete_soal.delete()

    return redirect("dosen:edit_quiz_materi", materi_id, matkul_id, quiz_id)
