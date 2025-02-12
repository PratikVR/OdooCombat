# Generated by Django 5.0.6 on 2024-06-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Administrator_db",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("Admin_dept", models.CharField(max_length=50)),
                ("phone_no", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=256)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Employee_db",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("emp_dept", models.CharField(max_length=50)),
                ("phone_no", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=256)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="grievance_db",
            fields=[
                (
                    "G_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("user_id", models.CharField(max_length=50)),
                ("G_title", models.CharField(max_length=100)),
                ("G_desc", models.TextField()),
                ("user_dept", models.CharField(max_length=100)),
                ("severity", models.IntegerField(max_length=3)),
                ("files", models.FileField(upload_to="G_media/")),
                ("register_time", models.TimeField(auto_now_add=True)),
                ("completion_time", models.TimeField(auto_now_add=True)),
                ("statue", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="HR_db",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("HR_dept", models.CharField(max_length=50)),
                ("phone_no", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=256)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
