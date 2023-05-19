# Generated by Django 4.2.1 on 2023-05-16 15:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="connection_user",
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
                ("username", models.CharField(max_length=128, unique=True)),
                ("connected_username", models.CharField(max_length=128, unique=True)),
                ("is_active", models.BooleanField(default=False, max_length=128)),
            ],
            options={"db_table": "connection",},
        ),
        migrations.CreateModel(
            name="users",
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
                ("username", models.CharField(max_length=128, unique=True)),
                ("full_name", models.CharField(db_column="full_name", max_length=200)),
                ("gender", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=120)),
                (
                    "interest",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255), size=10
                    ),
                ),
                ("email", models.EmailField(max_length=75, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                    ),
                ),
                (
                    "is_connected",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether this user is connected to the chat server",
                    ),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "users",},
        ),
    ]
