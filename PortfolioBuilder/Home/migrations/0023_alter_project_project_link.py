# Generated by Django 4.2 on 2023-06-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0022_rename_project_completing_date_project_project_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_link',
            field=models.URLField(blank=True, max_length=2084, null=True),
        ),
    ]
