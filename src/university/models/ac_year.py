from django.db import models


class AcademicYear(models.Model):
    """Defines the university academic year in a string format"""

    name = models.CharField(max_length=9, null=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "university_academic_year"
        ordering = ["name", "id"]
