from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создание")

    def __str__(self):
        return self.title