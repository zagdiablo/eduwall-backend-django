# Generated by Django 4.2.2 on 2023-10-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0011_alter_riwayatpengerjaanquiz_nilai"),
    ]

    operations = [
        migrations.AlterField(
            model_name="materi",
            name="url_video",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
