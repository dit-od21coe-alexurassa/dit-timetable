# Generated by Django 5.0 on 2023-12-14 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("general", "0001_initial"),
        ("university", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lecturer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=60)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("avatar", models.ImageField(max_length=275, upload_to="lecturers/")),
            ],
            options={
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
                ("code", models.CharField(max_length=12, unique=True)),
            ],
            options={
                "ordering": ["title", "code", "id"],
            },
        ),
        migrations.CreateModel(
            name="IntakeClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_code", models.CharField(max_length=20, unique=True)),
                (
                    "academic_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university.academicyear",
                    ),
                ),
            ],
            options={
                "db_table": "university_intake_class",
                "ordering": ["class_code"],
            },
        ),
        migrations.CreateModel(
            name="IntakeStream",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_code", models.CharField(max_length=20, unique=True)),
                (
                    "intake_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="university.intakeclass",
                    ),
                ),
            ],
            options={
                "db_table": "university_intake_stream",
                "ordering": ["class_code"],
            },
        ),
        migrations.CreateModel(
            name="Timetable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "academic_year",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="university.academicyear",
                    ),
                ),
                (
                    "intake_stream",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="university.intakestream",
                    ),
                ),
                (
                    "lecturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="university.lecturer",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="university.module",
                    ),
                ),
                (
                    "week_day",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="general.weekday",
                    ),
                ),
            ],
        ),
    ]
