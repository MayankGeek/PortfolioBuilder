# Generated by Django 4.2 on 2023-05-24 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_alter_skill_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='percent2',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill2',
        ),
    ]
