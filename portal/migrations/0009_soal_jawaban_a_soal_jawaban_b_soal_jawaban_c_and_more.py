# Generated by Django 4.2.2 on 2023-10-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0008_remove_matkul_dosen_pengampu_matkul_dosen_pengampu"),
    ]

    operations = [
        migrations.AddField(
            model_name="soal",
            name="jawaban_a",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="soal",
            name="jawaban_b",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="soal",
            name="jawaban_c",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="soal",
            name="jawaban_d",
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name="Jawaban",
        ),
    ]
