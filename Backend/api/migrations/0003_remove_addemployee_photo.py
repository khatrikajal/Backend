# Generated by Django 5.0.7 on 2024-07-29 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_addemployee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="addemployee",
            name="photo",
        ),
    ]
