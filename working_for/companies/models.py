from django.db import models

from users.models import User

from . import constants


class Company(models.Model):
    """ Модель компании (организации). """

    name = models.CharField(
        'Название компании',
        max_length=255,
        unique=True,
    )
    logo = models.ImageField(
        'Аватар',
        blank=True,
        null=True,
    )
    category = models.CharField(
        'Категория компании',
        max_length=50,
        choices=constants.COMPANY_CATEGORIES,
    )
    description = models.TextField(
        'Описание компании',
        blank=True,
        null=True,
    )
    location = models.CharField(
        'Местонахождение',
        max_length=50,
    )
    site = models.URLField(
        'Сайт компании',
        blank=True,
        null=True,
        unique=True,
    )
    creator = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Создатель компании',
        related_name='creator_of_the_company',
    )
    recruiters = models.ManyToManyField(
        User,
        verbose_name='Рекрутеры компании',
        related_name='recruiter_in',
    )
    is_blocked = models.BooleanField(
        'Блокировка компании',
        default=False,
    )

    def __str__(self):
        """ Строчное представление. """

        return self.name
