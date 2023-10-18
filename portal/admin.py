from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Role)
admin.site.register(models.Kelas)
admin.site.register(models.Matkul)
admin.site.register(models.Materi)
admin.site.register(models.Quiz)
admin.site.register(models.Soal)
admin.site.register(models.RiwayatPengerjaanQuiz)
