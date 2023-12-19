from django.db import models
from django.urls import reverse

from .intake_class import IntakeStream
from .ac_year import AcademicYear


class Timetable(models.Model):
    """
    No more than one timetable should be created for one intake stream in a semester of the
    same academic year.
    """

    SEM1 = 1
    SEM2 = 2

    SEMESTER_CHOICES = (("1", "Sem 1"), ("2", "Sem 2"))

    title = models.CharField(max_length=255, default="", editable=False)
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
        return reverse("university:timetables:detail", kwargs={"timetable_pk": self.pk})

    def __str__(self) -> str:
        return f"{self.academic_year.name}: {self.intake_stream}"

    def save(self, *args, **kwargs):
        # set title
        self.title = f"{self.intake_stream.stream_code} - {self.academic_year.name} (Sem {self.semester})"
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ["semester", "intake_stream", "academic_year"]
