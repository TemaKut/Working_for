# Generated by Django 4.1.3 on 2022-12-10 19:39

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='logo',
            field=models.ImageField(default='users/logo/default_logo/logo.jpg', upload_to=users.models.get_upload_path, verbose_name='Аватар'),
        ),
    ]
