# Generated by Django 2.2.16 on 2022-02-14 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220214_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='folowing',
            new_name='following',
        ),
    ]
