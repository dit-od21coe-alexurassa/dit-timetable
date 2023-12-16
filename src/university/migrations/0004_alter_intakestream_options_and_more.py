# Generated by Django 4.2 on 2023-12-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0003_alter_academicyear_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="intakestream",
            options={"ordering": ["stream_code"]},
        ),
        migrations.RenameField(
            model_name="intakestream",
            old_name="class_code",
            new_name="stream_code",
        ),
        migrations.AlterField(
            model_name="intakestream",
            name="intake_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="streams",
                to="university.intakeclass",
            ),
        ),
    ]
