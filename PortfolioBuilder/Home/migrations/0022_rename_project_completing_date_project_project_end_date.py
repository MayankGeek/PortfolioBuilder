# Generated by Django 4.2 on 2023-05-28 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0021_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_completing_date',
            new_name='project_end_date',
        ),
    ]
