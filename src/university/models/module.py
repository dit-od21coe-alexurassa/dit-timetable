from django.db import models
from django.urls import reverse


class Module(models.Model):

    title = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.title} ({ self.code })"
    
    def get_absolute_url(self):
        return reverse("university:modules:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['title', 'code', 'id']