# Generated by Django 4.1.1 on 2022-09-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_resumemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='user',
        ),
    ]
