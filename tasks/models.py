from django.db import models
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создание")
    deadline = models.DateField(blank=True, null=True, verbose_name="Дедлайн")
    is_finished = models.BooleanField(default=False, verbose_name="Завершено")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tasks")

    def __str__(self):
        return self.title