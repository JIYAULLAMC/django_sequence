# Generated by Django 4.1.5 on 2023-05-11 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=50)),
                ("area", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="school.company",
                    ),
                ),
                ("emp_name", models.CharField(max_length=100)),
                ("emp_salary", models.IntegerField()),
            ],
            bases=("school.company",),
        ),
    ]
