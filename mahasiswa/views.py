from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from portal import models
from . import forms


# Create your views here.
@login_required
def dashboard(request):
    account_data = get_object_or_404(models.Role, user_id=request.user.id)

    if account_data:
        # return render(
        #     request,
        #     "dashboard_mahasiswa.html",
        #     {"site_title": "Dashboard Mahasiswa", "account_data": account_data},
        # )
        # return render(
        #     request,
        #     "mahasiswa_base.html",
        #     {"site_title": "Dashboard Mahasiswa", "account_data": account_data},
        # )
        return redirect('mahasiswa:list_mata_kuliah')

    return redirect("portal:logout", kwargs={"site_title": "Login"})


@login_required
def edit_profile(request):
    account_data = get_object_or_404(models.Role, user=request.user)

    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, instance=account_data)
        if form.is_valid():
            account_data = form.save()
            # account_data.nama_lengkap = form.cleaned_data["nama_lengkap"]
            # account_data.nim = form.cleaned_data["nim"]
            account_data.save()

            return render( 
                request,
                "edit_profile_mahasiswa.html",
                {
                    "site_title": "Edit Profile",
                    "account_data": account_data,
                    "form": form,
                },
            )

    if account_data:
        form = forms.EditProfileForm()

        return render(
            request,
            "edit_profile_mahasiswa.html",
            {"site_title": "Edit Profile", "account_data": account_data, "form": form},
        )

    return redirect("portal:logout")


@login_required
def list_mata_kuliah(request):
    account_data = get_object_or_404(models.Role, user_id=request.user.id)
    kelas_data = get_object_or_404(models.Kelas, id=account_data.kelas_id)
    all_matkul = kelas_data.daftar_matkul.all()

    return render(
        request,
        "list_mata_kuliah_mahasiswa.html",
        {
            "account_data": account_data,
            "kelas_data": kelas_data,
            "all_matkul": all_matkul,
        },
    )


@login_required
def list_materi(request, matkul_id):
    matkul = get_object_or_404(models.Matkul, id=matkul_id)
    all_materi = models.Materi.objects.filter(matkul_id=matkul_id)

    return render(
        request, "matkul_mahasiswa.html", {"matkul": matkul, "all_materi": all_materi}
    )


@login_required
def konten_materi(request, materi_id):
    materi = get_object_or_404(models.Materi, id=materi_id)

    return render(request, "materi_mahasiswa.html", {"materi": materi})


@login_required
def modul_materi(request, materi_id):
    materi = get_object_or_404(models.Materi, id=materi_id)
    try:
        file_module = materi.file_materi.url
        return render(
            request,
            "modul_materi_mahasiswa.html",
            {"materi": materi, "file_module": file_module},
        )
    except Exception:
        return render(
            request,
            "modul_materi_mahasiswa.html",
            {"materi": materi, "file_module": None},
        )


@login_required
def quiz_materi(request, materi_id):
    materi = get_object_or_404(models.Materi, pk=materi_id)
    all_quiz = models.Quiz.objects.filter(materi=materi)

    return render(
        request, "quiz_materi_mahasiswa.html", {"materi": materi, "all_quiz": all_quiz}
    )


@login_required
def play_quiz(request, materi_id, quiz_id):
    materi = get_object_or_404(models.Materi, pk=materi_id)
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    account_data = get_object_or_404(models.Role, user=request.user)
    soal_list = get_list_or_404(models.Soal, quiz=quiz)
    quiz_soal_count = 0
    soal_benar = 0

    if request.method == "POST":
        for soal in soal_list:
            quiz_soal_count += 1
            jawaban = request.POST[f"jawaban_{soal.id}"]
            if jawaban == soal.jawaban_benar:
                soal_benar += 1
        nilai = (soal_benar / quiz_soal_count) * 100
        new_riwayat_pengerjaan_quiz = models.RiwayatPengerjaanQuiz()
        new_riwayat_pengerjaan_quiz.quiz = quiz
        new_riwayat_pengerjaan_quiz.mahasiswa = account_data
        new_riwayat_pengerjaan_quiz.nilai = nilai
        new_riwayat_pengerjaan_quiz.save()

        return redirect("mahasiswa:quiz_materi", materi_id)

    return render(
        request,
        "play_quiz_mahasiswa.html",
        {"materi": materi, "quiz": quiz, "soal_quiz": soal_list},
    )


@login_required
def nilai_quiz(request, materi_id):
    materi = get_object_or_404(models.Materi, pk=materi_id)
    account_data = get_object_or_404(models.Role, user=request.user)
    riwayat_pengerjaan_quiz = models.RiwayatPengerjaanQuiz.objects.filter(
        mahasiswa=account_data
    )

    return render(
        request,
        "nilai_mahasiswa.html",
        {
            "materi": materi,
            "account_data": account_data,
            "riwayat_pengerjaan_quiz": riwayat_pengerjaan_quiz,
        },
    )
