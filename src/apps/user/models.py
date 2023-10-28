from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from src.apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = (
        ('1', 'Admin'),
        ('2', 'Доктор'),
        ('3', 'Психолог'),
        ('4', 'Мед-Сестра'),
    )
    name = models.CharField(max_length=150, blank=True,)
    surname = models.CharField(max_length=150, blank=True,)
    phone = models.CharField(max_length=30, blank=True, null=True, unique=True,)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        default=False,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )
    role = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.name


