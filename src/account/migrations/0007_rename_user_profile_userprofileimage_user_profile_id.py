# Generated by Django 4.2.14 on 2024-07-12 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_rename_user_profile_id_userprofileimage_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileimage',
            old_name='user_profile',
            new_name='user_profile_id',
        ),
    ]