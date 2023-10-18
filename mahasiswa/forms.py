from django import forms
from django.forms import ModelForm
from portal import models


class EditProfileForm(ModelForm):
    class Meta:
        model = models.Role
        fields = {"nama_lengkap", "nim"}
