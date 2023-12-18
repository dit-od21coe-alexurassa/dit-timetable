from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class WeekDay(models.Model):
    name = models.CharField(max_length=8, unique=True)
    sort_order = models.IntegerField(
        default=0,
        unique=True,
        validators=[MinValueValidator(0), MaxValueValidator(6)],
        help_text="Lowest is 0 and highest should be 6",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "general_week_day"
        ordering = ["sort_order"]
