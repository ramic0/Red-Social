# Generated by Django 4.0.2 on 2023-03-02 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='username',
            new_name='usernames',
        ),
    ]