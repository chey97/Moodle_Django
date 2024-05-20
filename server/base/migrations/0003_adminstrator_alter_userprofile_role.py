# Generated by Django 4.2.13 on 2024-05-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adminstrator",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(blank=True, max_length=100)),
                ("contact_no", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="role",
            field=models.CharField(
                choices=[
                    ("teacher", "Teacher"),
                    ("student", "Student"),
                    ("admin", "Admin"),
                ],
                max_length=10,
            ),
        ),
    ]
