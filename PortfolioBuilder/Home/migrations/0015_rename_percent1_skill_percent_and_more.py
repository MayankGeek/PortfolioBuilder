# Generated by Django 4.2 on 2023-05-26 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_remove_skill_percent2_remove_skill_percent3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='percent1',
            new_name='percent',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='skill1',
            new_name='skill',
        ),
    ]