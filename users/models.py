from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name="Имя")

    def __str__(self):
        return self.full_name
