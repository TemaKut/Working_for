from django.db import models

from users.models import User


CATEGORY_IT = 'it'
CATEGORY_CATERING = 'catering'

COMPANY_CATEGORIES = [
    (CATEGORY_IT, 'IT'),
    (CATEGORY_CATERING, 'Catering'),
]


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
        choices=COMPANY_CATEGORIES,
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
    is_blocked = models.BooleanField(
        default=False,
    )
    recruiters = models.ManyToManyField(
        User,
        blank=True,
        null=True,
        verbose_name='recruiters',
        related_name='companies',
    )

    def __str__(self):
        """ Строчное представление. """

        return self.name