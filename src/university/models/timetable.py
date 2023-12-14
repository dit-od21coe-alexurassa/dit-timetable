from django.db import models
from general.models import WeekDay

from .lecturer import Lecturer
from .intake_class import IntakeStream
from .ac_year import AcademicYear
from .module import Module


class Timetable(models.Model):
    lecturer = models.ForeignKey(to=Lecturer, on_delete=models.SET_NULL, null=True)
    intake_stream = models.ForeignKey(
        to=IntakeStream, on_delete=models.SET_NULL, null=True
    )
    academic_year = models.ForeignKey(
        to=AcademicYear, on_delete=models.SET_NULL, null=True
    )
    module = models.ForeignKey(to=Module, on_delete=models.SET_NULL, null=True)
    week_day = models.ForeignKey(to=WeekDay, on_delete=models.SET_NULL, null=True)
