# Generated by Django 5.0.6 on 2024-06-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grievance_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="administrator_db",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="employee_db",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="hr_db",
            name="last_login",
        ),
        migrations.AlterField(
            model_name="grievance_db",
            name="severity",
            field=models.IntegerField(),
        ),
    ]
