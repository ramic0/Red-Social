# Generated by Django 4.0.2 on 2023-03-05 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_rename_username_perfil_usernames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='usernames',
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
