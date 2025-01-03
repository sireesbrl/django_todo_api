# Generated by Django 5.1.4 on 2024-12-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="is_completed",
        ),
        migrations.AddField(
            model_name="todo",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "Completed"),
                    ("in_progress", "In Progress"),
                    ("draft", "Draft"),
                ],
                default="Draft",
                max_length=20,
            ),
        ),
    ]
