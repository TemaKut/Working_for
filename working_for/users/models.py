from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from . import constants
from .source import get_upload_path


class User(AbstractUser):
    """ Переопределяем поля пользователя. """
    logo = models.ImageField(
        'Аватар',
        upload_to=get_upload_path,
        default='users/logo/default_logo/logo.jpg',
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    password = models.CharField(
        'Пароль',
        max_length=100,
    )
    role = models.CharField(
        "Роль",
        max_length=30,
        choices=constants.USER_ROLES,
        default=constants.APPLICANT,
    )
    location = models.CharField(
        'Местонахождение',
        max_length=50,
        blank=True,
        null=True,
    )
    is_blocked = models.BooleanField(
        'Блокировка пользователя',
        default=False,
    )

    @property
    def is_admin(self):
        """ Является ли пользователь представителем администрации. """

        return (
            constants.ADMIN in self.role
            or self.is_staff
            or self.is_superuser
        )

    @property
    def is_employer(self):
        """ Является ли пользователь работодателем. """

        return constants.EMPLOYER in self.role

    @property
    def is_applicant(self):
        """ Является ли пользователь соискателем. """

        return constants.APPLICANT in self.role

    def __str__(self):
        """ Строчное представление. """

        return self.username
