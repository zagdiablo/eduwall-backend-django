# Generated by Django 4.2.2 on 2023-10-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0010_alter_soal_jawaban_a_alter_soal_jawaban_b_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="riwayatpengerjaanquiz",
            name="nilai",
            field=models.FloatField(),
        ),
    ]