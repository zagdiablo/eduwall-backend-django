from django.forms import ModelForm
from portal import models
from django import forms


class TambahMateriForm(ModelForm):
    class Meta:
        model = models.Materi
        exclude = (
            "dosen_pembuat",
            "matkul",
            "video_text_transcript",
        )

    judul_materi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Judul Materi",
            }
        )
    )
    url_video = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "URL Video",
            }
        )
    )
    link_materi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Link File Materi",
            }
        )
    )


class EditMateriForm(ModelForm):
    class Meta:
        model = models.Materi
        exclude = (
            "dosen_pembuat",
            "matkul",
            "video_text_transcript",
        )

    judul_materi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Judul Materi",
            }
        )
    )
    url_video = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "URL Video",
            }
        )
    )
    link_materi = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Link File Materi",
            }
        )
    )


class EditQuizForm(ModelForm):
    class Meta:
        model = models.Quiz
        exclude = (
            "materi",
            "dibuat_oleh",
        )

    judul_quiz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Judul Quiz",
            }
        )
    )
    waktu_pengerjaan = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Waktu Pengerjaan",
            }
        )
    )


class EditSoalForm(ModelForm):
    class Meta:
        model = models.Soal
        exclude = ("quiz",)

    text_soal = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Text Soal",
            }
        )
    )
    jawaban_a = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Jawaban A",
            }
        )
    )
    jawaban_b = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Jawaban B",
            }
        )
    )
    jawaban_c = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Jawaban C",
            }
        )
    )
    jawaban_d = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Jawaban D",
            }
        )
    )
    jawaban_benar = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "basicInput",
                "placeholder": "Jawaban Benar",
            }
        )
    )
