# Generated by Django 4.2.2 on 2024-03-03 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0008_task_file_upload_task_image_upload"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"permissions": [("custom_task", "Custom Task Permission")]},
        ),
    ]
