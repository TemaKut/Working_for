# Generated by Django 4.1.3 on 2022-12-09 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_remove_company_recruiters_company_recruiters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='recruiters',
            field=models.ManyToManyField(blank=True, null=True, related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='recruiters'),
        ),
    ]