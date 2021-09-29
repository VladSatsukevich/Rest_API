from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class Message(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)
    text_of_problem = models.TextField()
    STATUS = (
        ('Нерешен', 'Нерешен'),
        ('Решен', 'Решен'),
        ('Замарожен', 'Замарожен'),
    )
    status = models.CharField(max_length=120, default='Нерешен', choices=STATUS)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Укажите логин')
        if email is None:
            raise TypeError('Укажите почту')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Укажите пароль')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

