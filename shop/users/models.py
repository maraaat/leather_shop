from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Email")
    username = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=150, null=True, blank=True, verbose_name='Пароль')
    fio = models.CharField(max_length=250, null=True, blank=True, verbose_name='ФИО')
    phone = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер телефона')

    class Meta:
        db_table = 'users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]

    def __str__(self):
        return self.username