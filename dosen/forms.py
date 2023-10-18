from django.forms import ModelForm
from portal import models


class EditMateriForm(ModelForm):
    class Meta:
        model = models.Materi
        exclude = (
            "dosen_pembuat",
            "matkul",
            "video_text_transcript",
        )


class EditQuizForm(ModelForm):
    class Meta:
        model = models.Quiz
        exclude = (
            "materi",
            "dibuat_oleh",
        )


class EditSoalForm(ModelForm):
    class Meta:
        model = models.Soal
        exclude = ("quiz",)
