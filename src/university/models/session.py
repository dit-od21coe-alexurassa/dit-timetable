from django.db import models
from django.utils import timezone
from django.urls import reverse
from general.models import WeekDay

from .lecturer import Lecturer
from .module import Module

from .timetable import Timetable


class Session(models.Model):
    """For each instance of a session. Each session must have a unique together relationship
    between a lecturer, module and it's related timetable. With that means no lecturer couuld have
    multiple copies of the same module within the same timetable.
    """

    timetable = models.ForeignKey(to=Timetable, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(to=Lecturer, on_delete=models.SET_NULL, null=True)
    module = models.ForeignKey(to=Module, on_delete=models.SET_NULL, null=True)
    week_day = models.ForeignKey(to=WeekDay, on_delete=models.SET_NULL, null=True)
    venue = models.CharField(max_length=145)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(null=False)

    def get_absolute_url(self):
        return reverse("university:academic_years:timetables", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.pk} -> {self.timetable.intake_stream}"

    class Meta:
        unique_together = ["timetable", "lecturer", "module"]
