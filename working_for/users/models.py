from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

ADMIN = "admin"
EMPLOYER = "employer"
APPLICANT = "applicant"

USER_ROLES = (
    (ADMIN, "Administrator"),
    (EMPLOYER, "Employer"),
    (APPLICANT, "Applicant"),
)


class User(AbstractUser):
    """ Переопределяем поля пользователя. """
    logo = models.ImageField(
        'Аватар',
        blank=True,
        null=True,
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
        choices=USER_ROLES,
        default=APPLICANT,
    )
    location = models.CharField(
        'Местонахождение',
        max_length=50,
        blank=True,
        null=True,
    )
    is_blocked = models.BooleanField(
        default=False,
    )

    @property
    def is_admin(self):

        return (
            ADMIN in self.role
            or self.is_staff
            or self.is_superuser
        )

    @property
    def is_employer(self):

        return EMPLOYER in self.role

    @property
    def is_applicant(self):

        return APPLICANT in self.role
