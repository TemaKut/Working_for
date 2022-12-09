# Generated by Django 4.1.3 on 2022-12-09 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='company',
            name='recruiters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recruiters', to=settings.AUTH_USER_MODEL, verbose_name='recruiters'),
        ),
    ]
