from django.db import models


class Module(models.Model):

    title = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.title} ({ self.code })"

    class Meta:
        ordering = ['title', 'code', 'id']