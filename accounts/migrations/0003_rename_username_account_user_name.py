# Generated by Django 3.2.5 on 2022-04-19 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_user_name_account_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='username',
            new_name='user_name',
        ),
    ]
