# Generated by Django 4.2 on 2023-05-26 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_skill_percent3_skill_percent4_skill_percent5_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='percent2',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='percent3',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='percent4',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='percent5',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill2',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill3',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill4',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skill5',
        ),
    ]