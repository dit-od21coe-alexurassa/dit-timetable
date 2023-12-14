from django.db import models
from django.urls import reverse

from .ac_year import AcademicYear

class IntakeClass(models.Model):

    academic_year = models.ForeignKey(to=AcademicYear, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=20, unique=True)


    def __str__(self) -> str:
        return self.class_code
    
    def get_absolute_url(self):
        return reverse("university:intake_classes:detail", kwargs={"class_pk": self.pk})
    

    class Meta:
        ordering = ['class_code']
        db_table = 'university_intake_class'


class IntakeStream(models.Model):

    intake_class = models.ForeignKey(to=IntakeClass, on_delete=models.CASCADE)
    class_code = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.class_code
    
    def get_absolute_url(self):
        return reverse("university:intake_classes:streams:detail", kwargs={"class_pk": self.intake_class.pk, "stream_pk": self.pk})
    
    class Meta:
            ordering = ['class_code']
            db_table = "university_intake_stream"