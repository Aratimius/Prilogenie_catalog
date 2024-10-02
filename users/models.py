from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='страна', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/photo', verbose_name='аватар', blank=True, null=True)

    # Для верификации почты ползователя:
    token = models.CharField(max_length=100, verbose_name='token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


