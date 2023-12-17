from django.db import models
from django.urls import reverse

from .intake_class import IntakeStream
from .ac_year import AcademicYear


class Timetable(models.Model):
    SEM1 = 1
    SEM2 = 2

    SEMESTER_CHOICES = (("1", "Sem 1"), ("2", "Sem 2"))
    SEMESTER_CHOICES[SEM1]
    intake_stream = models.ForeignKey(
        to=IntakeStream, on_delete=models.SET_NULL, null=True
    )
    academic_year = models.ForeignKey(
        to=AcademicYear, on_delete=models.SET_NULL, null=True
    )
    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES,
        default="1",
        help_text="Each academic year has a maximum of 2 semesters, defaults to 1",
    )

    def get_absolute_url(self):
        return reverse(
            "university:academic_years:timetables:detail", kwargs={"pk": self.pk}
        )

    def __str__(self) -> str:
        return f"{self.academic_year.name}: {self.intake_stream}"
