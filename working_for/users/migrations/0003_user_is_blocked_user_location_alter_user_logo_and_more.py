# Generated by Django 4.1.3 on 2022-12-08 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Местонахождение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
    ]
