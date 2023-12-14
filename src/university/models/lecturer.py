from django.db import models


class Lecturer(models.Model):

    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.ImageField(max_length=275, upload_to='lecturers/')

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        ordering = ['full_name']