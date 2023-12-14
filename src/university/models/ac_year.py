from django.db import models
from django.urls import reverse


class AcademicYear(models.Model):
    """Defines the university academic year in a string format"""

    name = models.CharField(
        max_length=9, null=False, unique=True, help_text="Eg. 2023/24 or 2023/2024"
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("university:academic_years:detail", kwargs={"pk": self.pk})

    class Meta:
        db_table = "university_academic_year"
        ordering = ["name", "id"]
