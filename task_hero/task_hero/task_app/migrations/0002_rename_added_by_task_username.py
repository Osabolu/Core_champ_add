# Generated by Django 5.1.3 on 2024-11-13 11:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="added_by",
            new_name="username",
        ),
    ]
