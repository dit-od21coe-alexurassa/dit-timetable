from django.db import models


class WeekDay(models.Model):
    name = models.CharField(max_length=8, unique=True)
    sort_order = models.IntegerField(default=0, unique=True)

    class Meta:
        db_table = "general_week_day"
        ordering = ["sort_order"]
