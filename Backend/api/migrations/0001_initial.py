# Generated by Django 5.0.7 on 2024-07-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(unique=True)),
                ("password", models.CharField(max_length=20)),
                ("repassword", models.CharField(max_length=20)),
            ],
        ),
    ]
